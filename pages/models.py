from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel


class PublishedPage(models.Manager):
    def published(self):
        return self.filter(status="pub")


class Page(TimeStampedModel):
    class Meta:
        verbose_name = "برگه"
        verbose_name_plural = "برگه ها"
    STATUS_CHOICES = (
        ("pub", "منتشر شده"),
        ("dra", "پیش نویس"),
        ("del", "زباله دان"),
    )
    title = models.CharField(max_length=50, verbose_name="عنوان برگه")
    slug = models.SlugField(blank=True, unique=True, max_length=25, allow_unicode=True, verbose_name="نامک")
    description = models.TextField(max_length=5000, verbose_name="محتوا")
    published = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, verbose_name="وضعیت انتشار")

    def __str__(self):
        return self.title

    objects = PublishedPage()
