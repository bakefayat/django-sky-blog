from django.db import models


class Module(models.Model):
    class Meta:
        verbose_name = "ابزارک"
        verbose_name_plural = "ابزارک ها"
        ordering = ["position", "order"]

    POSITION_CHOICES = (
        ("top", "بالا"),
        ("left", "چپ"),
        ("foot1", "پایین راست"),
        ("foot2", "پایین وسط"),
        ("foot3", "پایین چپ"),
    )
    title = models.CharField(max_length=250, verbose_name="عنوان ابزارک")
    body = models.TextField(max_length=1000, verbose_name="کد")
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, verbose_name="جایگاه")
    order = models.IntegerField(verbose_name="ترتیب")
    display = models.BooleanField(default=True, verbose_name="نمایش")

    def __str__(self):
        return self.title
