from django.contrib import admin
from .models import Module


class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "position", "order", "display")
    list_filter = ["display"]


admin.site.register(Module, ModuleAdmin)
