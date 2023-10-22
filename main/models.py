from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()

from django.template.defaultfilters import slugify
import os

class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    subtitle = models.CharField(max_length=200, default="", blank=True, verbose_name="Qo'shimcha sarlavha") 
    slug = models.SlugField("Slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255, verbose_name='Rasm')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title = models.CharField(max_length=200, verbose_name="Mavzu sarlavhasi")
    subtitle = models.CharField(max_length=200, default="", blank=True, verbose_name="Mavzu haqida qisqacha ma'lumot")
    article_slug = models.SlugField("Article slug", null=False, blank=False, unique=True)
    content = HTMLField(blank=True, default="", verbose_name="Mazvu haqida to'liq shu yerda yoritib berishingiz mumkin")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="Qaysi bo'limga tegishli", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255, verbose_name="Rasm qo'yish shart")

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']