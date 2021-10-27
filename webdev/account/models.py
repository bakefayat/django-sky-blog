from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name='نویسنده')
    special_user = models.DateTimeField(default=timezone.now, verbose_name='ویژه تا', )
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    def is_specialuser(self):
        if self.special_user > timezone.now():
            return True
        return False
    is_specialuser.short_description = 'کاربر ویژه'
    is_specialuser.boolean = True