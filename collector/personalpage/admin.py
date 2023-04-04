from django.contrib import admin
from .models import NewArticle


class NewArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'text', 'photo']
admin.site.register(NewArticle, NewArticleAdmin)    

