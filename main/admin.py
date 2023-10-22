from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        'author',
        'image',
        # 'published'
    ]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Header", {"fields": ['title', 'subtitle', 'article_slug', 'series', 'author', 'image']}),
        ("Content", {"fields": ['content', 'notes']}),
        ("Date", {"fields": ['modified']})
    ]

# Register your models here.
