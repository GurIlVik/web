from django.contrib import admin
from .models import *


class NewArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'text', 'photo']   # список полей которые необходимы в админке
    list_display_links = ('id', 'author', 'title',)             # список полей в админке кликабельные
    search_fields = ('title', 'author', )                       # список полей в админке для поиска
    list_editable = ('text',)                                    # список полей в админке которые возможны к редакции
    list_filter = ('title', 'author', )                         # список полей в админке по которым можно фильтровать
#    prepopulated_fields = {'slug': ('name',)}                   # необходимо для автоматического заполнения, но может быть повтор по этому лучше ID
#    prepopulated_fields = {'slug': (f'{NewArticle.title}_{NewArticle.id}')}                   # проба
    fields = ('title', 'author', 'text',)                       # порядок и список редактируемых полей в форме представления статьи
    readonly_fields = ('author', 'photo')                       # порядок и список НЕ редактируемых полей 
    save_on_top = True                                          # дублирует работающее меню на верх 
admin.site.register(NewArticle, NewArticleAdmin)    

# class InfoUserAdmin(admin.ModelAdmin):
#     list_display = ['user', 'profession', 'FFP', 'interest', 'in_publishid']
#     search_fields = ('user', 'profession', 'FFP',)
#     list_filter = ('user', 'profession', 'FFP',)
# admin.site.register(InfoUser, InfoUserAdmin)  

# class ProfessionalAdmin(admin.ModelAdmin):
#     list_display = ['name'] 
#     fields = ('name',) 
#     readonly_fields = ('name',)
#     search_fields = ('name',)
#     list_filter = ('name',)
# admin.site.register(Professional, ProfessionalAdmin)    

class AllowanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'for_page', 'for_inform', 'for_messeng', 'in_publishid',]
admin.site.register(Allowance, AllowanceAdmin)

class PresentationUserAdmin(admin.ModelAdmin):
    list_display = ['user', 
                    # 'nikname', 
                    'photo', 'profession', 'FFP', 'interest', 'in_publishid',]
admin.site.register(PresentationUser, PresentationUserAdmin)

class InfoUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'name_last', 'name_first', 'telephon', 'in_publishid']
admin.site.register(InfoUser, InfoUserAdmin)


admin.site.register(Professional)   
admin.site.register(AllowanceModel)
admin.site.register(AllowanceModel1)
admin.site.register(AllowanceModel2)
admin.site.register(AllowanceModel3)
admin.site.register(Photo)
