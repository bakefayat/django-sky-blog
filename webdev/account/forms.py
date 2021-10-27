from django import forms
from .models import User
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['is_author'].disabled = True
            self.fields['special_user'].disabled = True
    
    class Meta:
        fields = [
            'username', 'first_name', 'last_name', 'email', 'is_author', 'special_user'
        ]
        model = User
