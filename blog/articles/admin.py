from django.contrib import admin

from .models import Article
from .models import Article2

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
class ArticleAdmin2(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
admin.site.register(Article, ArticleAdmin)
admin.site.register(Article2, ArticleAdmin2)