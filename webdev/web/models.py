from django.db import models
from account.models import User
from django.db.models.deletion import SET_NULL
from django.utils import timezone
from django.utils.html import format_html
from extentions.utils import to_jalali
from django.urls import reverse


class PublishedArticle(models.Manager):
    def published(self):
        return self.filter(status='p')

class ShownCategory(models.Manager):
    def shown(self):
        return self.filter(display=True)


class Category(models.Model):
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering = ['parent__id', 'position']


    def __str__(self):
        return self.title

    title = models.CharField(max_length=255, default='', verbose_name='دسته بندی')
    parent = models.ForeignKey('self', related_name='children', default=None, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='دسته والد')
    slug = models.SlugField(max_length=20, unique=True, allow_unicode=True, verbose_name='نامک')
    display = models.BooleanField(verbose_name='نمایش', default=True, )
    position = models.IntegerField(verbose_name='جایگاه', default='0')

    objects = ShownCategory()

class Blog(models.Model):
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-published']


    def __str__(self):
        return self.title

    STATUS_CHOICES = (
        ('d', 'پیش نویس'),
        ('p', 'منتشر شده'),
        ('w', 'در انتظار تایید'),
        ('r', 'رد شده'),
    )
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(unique=True, max_length=20, allow_unicode=True,verbose_name='نامک')
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='نویسنده')
    description = models.TextField(max_length=1000,verbose_name='توضیحات')
    image = models.ImageField(upload_to='images',verbose_name='تصویر شاخص')
    published = models.DateTimeField(default= timezone.now,verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت')
    updated = models.DateTimeField(auto_now=True,verbose_name='آخرین بروزرسانی')
    is_special = models.BooleanField(verbose_name='مقاله ویژه', default=False, )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,verbose_name='وضعیت')
    category = models.ManyToManyField(Category, related_name='articles' , verbose_name='دسته بندی')

    
    def categoryList(self):
        return '، '.join([i.title for i in self.category.shown()])


    def jpublished(self):
        return to_jalali(self.published)

    def thumb(self):
        return format_html(f"<img src='{self.image.url}' height=80px width=100px style='border-radius:20px;'>")

    def get_absolute_url(self):
        return reverse('account:list')

    objects = PublishedArticle()

    jpublished.short_description = 'زمان انتشار'
    categoryList.short_description = 'دسته بندی'
    thumb.short_description = 'تصویر بندانگشتی'
