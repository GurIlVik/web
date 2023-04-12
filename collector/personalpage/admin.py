from django.contrib import admin
from .models import NewArticle


class NewArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'text', 'photo']   # список полей которые необходимы в админке
    list_display_links = ('id', 'author', 'title',)             # список полей в админке кликабельные
    search_fields = ('title', 'author', )                       # список полей в админке для поиска
    list_editable = ('text',)                                    # список полей в админке которые возможны к редакции
    list_filter = ('title', 'author', )                         # список полей в админке по которым можно фильтровать
#    prepopulated_fields = {'slug': ('name',)}                   # необходимо для автоматического заполнения, но может быть повтор по этому лучше ID
#    prepopulated_fields = {'slug': (f'{NewArticle.title}_{NewArticle.id}')}                   # проба
admin.site.register(NewArticle, NewArticleAdmin)    

