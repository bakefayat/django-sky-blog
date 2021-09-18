from django.http import Http404
class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_staff:
            self.fields = [
                'title' , 'slug' , 'author' , 'description' , 'image' , 'published' , 'status' , 'category'
            ]
        elif request.user.is_author:
            self.fields = [
                'title' , 'slug' , 'description' , 'image' , 'category', 'published'
            ]
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser or self.request.user.is_staff:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)
