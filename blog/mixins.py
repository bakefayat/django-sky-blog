from extensions.utils import check_staff_superuser


class CommentFormValidMixin:
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        if check_staff_superuser(self.request):
            self.obj.display = True
        else:
            self.obj.display = False
        return super().form_valid(form)
