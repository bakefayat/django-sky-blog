from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        post = kwargs.pop("post")
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["post"].initial = post
        self.fields["post"].disabled = True

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'post')
