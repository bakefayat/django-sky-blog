from django.contrib.admin.models import LogEntry
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

from extensions.utils import to_jalali


class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name="نویسنده")
    special_user = models.DateTimeField(
        default=timezone.now,
        verbose_name="ویژه تا",
    )
    email = models.EmailField(unique=True, verbose_name="ایمیل")

    def is_specialuser(self):
        if self.special_user > timezone.now() or self.is_superuser:
            return True
        return False

    is_specialuser.short_description = "کاربر ویژه"
    is_specialuser.boolean = True


class Logs(models.Model):
    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"

    log = models.OneToOneField(LogEntry, on_delete=models.CASCADE, verbose_name="رویداد")

    def jpublished(self):
        return to_jalali(self.log.action_time)

    jpublished.short_description = "زمان رویداد"


@receiver(post_save, sender=LogEntry)
def create_medical_history(sender, instance, created, **kwargs):
    if created:
        Logs.objects.create(log=instance)
