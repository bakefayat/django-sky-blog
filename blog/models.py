from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from hitcount.models import HitCount
from extensions.utils import to_jalali, unique_slug
from accounts.models import User
from core.models import TimeStampedModel


class PublishedArticle(models.Manager):
    def published(self):
        return self.filter(status="p")


class ShownCategory(models.Manager):
    def shown(self):
        return self.filter(display=True)


class PublishedComment(models.Manager):
    def published(self):
        return self.filter(display=True)


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["parent__id", "position"]

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, default="", verbose_name="دسته بندی")
    parent = models.ForeignKey(
        "self",
        related_name="children",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="دسته والد",
    )
    slug = models.SlugField(
        max_length=20, unique=True, allow_unicode=True, verbose_name="نامک"
    )
    display = models.BooleanField(
        verbose_name="نمایش",
        default=True,
    )
    position = models.IntegerField(verbose_name="جایگاه", default="0")

    objects = ShownCategory()

    def get_absolute_url(self):
        return reverse("accounts:cat_detail", kwargs={"slug": self.slug})


class Blog(TimeStampedModel):
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ["-published"]

    STATUS_CHOICES = (
        ("d", "پیش نویس"),
        ("p", "منتشر شده"),
        ("w", "در انتظار تایید"),
        ("r", "رد شده"),
    )
    title = models.CharField(max_length=255, verbose_name="عنوان")
    slug = models.SlugField(
        blank=True, unique=True, max_length=20, allow_unicode=True, verbose_name="نامک"
    )
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="articles",
        verbose_name="نویسنده",
    )
    description = models.TextField(max_length=1000, verbose_name="توضیحات")
    image = models.ImageField(upload_to="images", verbose_name="تصویر شاخص")
    published = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    is_special = models.BooleanField(
        verbose_name="مقاله ویژه",
        default=False,
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    category = models.ManyToManyField(Category, related_name="articles", verbose_name="دسته بندی")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count')

    def category_list(self):
        return "، ".join([i.title for i in self.category.shown()])

    def jpublished(self):
        return to_jalali(self.published)

    def thumb(self):
        return format_html(
            f"<img src='{self.image.url}' height=80px width=100px style='border-radius:20px;'>"
        )

    def __str__(self):
        return self.title

    def show_url(self):
        if self.slug:
            url = reverse("blog:single", kwargs={"slug": self.slug})
            response = format_html(f'<a href="{url}">{self.title}</a>')
            return response
        return 'برای مشاهده لینک مقاله ابتدا باید آن را منشتر کنید.'

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        # avoid regenerating slug.
        if not self.pk:
            title = self.title
            max_length = self._meta.get_field('slug').max_length
            self.slug = unique_slug(title, max_length, Blog)
        super().save(*args, **kwargs)

    objects = PublishedArticle()

    jpublished.short_description = "زمان انتشار"
    category_list.short_description = "دسته بندی"
    thumb.short_description = "تصویر بندانگشتی"
    show_url.short_description = "نمایش مقاله"


class Comment(TimeStampedModel):
    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        ordering = ["created"]

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments", verbose_name="نظر")
    name = models.CharField(max_length=50, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.TextField(max_length=1000, verbose_name="متن نظر")
    display = models.BooleanField(
        verbose_name="نمایش",
        default=False,
    )

    def __str__(self):
        return self.body

    def jpublished(self):
        return to_jalali(self.created)

    def get_absolute_url(self):
        return reverse("blog:comment", kwargs={"slug": self.post.slug})

    objects = PublishedComment()
