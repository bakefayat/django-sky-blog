from extensions.utils import check_staff_superuser


class CommentFieldsMixin:
    def dispatch(self, request, *args, **kwargs):
        self.fields = [
            "name",
            "email",
            "body",
        ]
        return super().dispatch(request, *args, **kwargs)


class CommentFormValidMixin:
    def form_valid(self, form):
        if check_staff_superuser(self.request):
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.display = False
        return super().form_valid(form)
