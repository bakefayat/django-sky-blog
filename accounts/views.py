from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from blog.models import Blog, Category
from .models import User
from .forms import ProfileForm
from .mixins import FieldsMixin, FormValidMixin, UpdateAccessMixin, DraftEditMixin, DeleteArticleMixin, PreviewMixin,\
    AuthorsMixin, ActionMixin, StaffMixin


class Login(LoginView):
    template_name = "accounts/login.html"

    def get_success_url(self):
        if (
            self.request.user.is_superuser
            or self.request.user.is_staff
            or self.request.user.is_author
        ):
            return reverse_lazy("accounts:list")
        else:
            return reverse_lazy("accounts:profile")


class HomeView(LoginRequiredMixin, AuthorsMixin, TemplateView):
    template_name = "accounts/admin.html"


class ArticleListView(LoginRequiredMixin, AuthorsMixin, ListView):
    template_name = "accounts/articleList.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(author=self.request.user)


class ArticleCreateView(
    LoginRequiredMixin, AuthorsMixin, ActionMixin, FormValidMixin, FieldsMixin, CreateView
):
    model = Blog
    template_name = "accounts/articleCreate.html"
    success_message = "مقاله با موفقیت ساخته شد."


class ArticleUpdateView(
    LoginRequiredMixin,
    AuthorsMixin,
    ActionMixin,
    DraftEditMixin,
    UpdateAccessMixin,
    FormValidMixin,
    FieldsMixin,
    UpdateView,
):
    model = Blog
    template_name = "accounts/articleUpdate.html"
    success_message = "با موفقیت بروزرسانی شد."


# show updated or created successfully message
class ArticleDetailView(ActionMixin, DetailView):
    model = Blog
    template_name = "accounts/article_detail.html"


class ArticleDeleteView(LoginRequiredMixin, AuthorsMixin, DeleteArticleMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("accounts:list")
    template_name = "accounts/articleDelete.html"


class ArticlePreviewView(PreviewMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Blog, slug=slug)

    template_name = "blog/article_Detail.html"


class CategoryListView(LoginRequiredMixin, StaffMixin, ListView):
    template_name = "accounts/category_list.html"
    queryset = Category.objects.all()


class CategoryCreateView(
    LoginRequiredMixin, StaffMixin, ActionMixin, CreateView
):
    fields = "__all__"
    model = Category
    template_name = "accounts/category_create.html"
    success_message = "دسته بندی با موفقیت ساخته شد."


# show updated or created successfully message
class CategoryDetailView(LoginRequiredMixin, StaffMixin, ActionMixin, DetailView):
    model = Category
    template_name = "accounts/article_detail.html"


class CategoryUpdateView(
    LoginRequiredMixin,
    StaffMixin,
    ActionMixin,
    UpdateView,
):
    model = Category
    fields = "__all__"
    template_name = "accounts/category_update.html"
    success_message = "با موفقیت بروزرسانی شد."


class CategoryDeleteView(LoginRequiredMixin, StaffMixin, ActionMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("accounts:cat_list")
    template_name = "accounts/category_delete.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    model = User
    template_name = "accounts/profileUpdate.html"
    success_url = reverse_lazy("accounts:profile")
    form_class = ProfileForm


from django.http import HttpResponse
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class RegisterCreateView(CreateView):
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = "Activate your blog accounts."
        message = render_to_string(
            "accounts/acc_active_email.html",
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            },
        )
        to_email = form.cleaned_data.get("email")
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        return redirect("register-pending")

    form_class = SignupForm
    template_name = "accounts/register_form.html"


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return redirect("register-complete")
    else:
        return HttpResponse("فعالسازی اکانت ناموفق بود.")
