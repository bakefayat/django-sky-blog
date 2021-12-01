from django.http import request, response
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.list import ListView
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from web.models import Blog
from .models import User
from .forms import ProfileForm
from .mixins import (
    DeleteArticleMixin,
    FieldsMixin,
    FormValidMixin,
    UpdateAccessMixin,
    DraftEditMixin,
    DeleteArticleMixin,
    PreviewMixin,
    AuthorsMixin,
)


class Login(LoginView):
    def get_success_url(self):
        if (
            self.request.user.is_superuser
            or self.request.user.is_staff
            or self.request.user.is_author
        ):
            return reverse_lazy("account:list")
        else:
            return reverse_lazy("account:profile")


class Home(LoginRequiredMixin, AuthorsMixin, TemplateView):
    template_name = "registration/admin.html"


class ArticleList(LoginRequiredMixin, AuthorsMixin, ListView):
    template_name = "registration/articleList.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(author=self.request.user)


class CreateArticle(
    LoginRequiredMixin, AuthorsMixin, FormValidMixin, FieldsMixin, CreateView
):
    model = Blog
    template_name = "registration/articleCreate.html"


class UpdateArticle(
    LoginRequiredMixin,
    AuthorsMixin,
    DraftEditMixin,
    UpdateAccessMixin,
    FormValidMixin,
    FieldsMixin,
    UpdateView,
):
    model = Blog
    template_name = "registration/articleUpdate.html"


class DeleteArticle(LoginRequiredMixin, AuthorsMixin, DeleteArticleMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("account:list")
    template_name = "registration/articleDelete.html"


class PreviewArticle(PreviewMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Blog, slug=slug)

    template_name = "blog/articleDetail.html"


class UpdateProfile(LoginRequiredMixin, UpdateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    model = User
    template_name = "registration/profileUpdate.html"
    success_url = reverse_lazy("account:profile")
    form_class = ProfileForm


from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class Register(CreateView):
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = "Activate your blog account."
        message = render_to_string(
            "registration/acc_active_email.html",
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
    template_name = "registration/register_form.html"


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
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
