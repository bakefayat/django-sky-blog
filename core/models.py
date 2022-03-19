from django.contrib.sites.models import Site
from django.db import models


class SiteProfile(models.Model):

    title = models.CharField(max_length=100, verbose_name="عنوان سایت")
    description = models.TextField(max_length=200, verbose_name="توضیحات سایت")
    site = models.OneToOneField(Site, on_delete=models.SET_NULL, null=True, verbose_name="آدرس سایت")

    class Meta:
        verbose_name = "تنظیم سایت"
        verbose_name_plural = "تنظیمات سایت"

    def __str__(self):
        return self.title


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    modified = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        abstract = True
