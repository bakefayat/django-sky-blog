from django.contrib import admin
from .models import User
# Register your models here.
class UserAdminPanel(admin.ModelAdmin):
    list_display = ['username', 'user_full_name', 'is_superuser', 'is_staff', 'is_author', 'is_specialuser']
    
    def user_full_name(self, obj):
        return obj.get_full_name()
    user_full_name.short_description = 'نام کاربر'

admin.site.register(User, UserAdminPanel)
