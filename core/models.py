from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    modified = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        abstract = True
