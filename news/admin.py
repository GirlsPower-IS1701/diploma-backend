from django.contrib import admin
from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'body')
    search_fields = ['title', 'body']
admin.site.register(News, NewsAdmin)