from django.contrib import admin
from pages.models import Page
# Register your models here.


class PagesAdmin(admin.ModelAdmin):
    list_display = ("title", "description")


admin.site.register(Page, PagesAdmin)
