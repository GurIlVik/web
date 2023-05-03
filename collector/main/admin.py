from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):   # ОСНОВНОЙ СПИСОК ПРЕДМЕТОВ КОЛЛЕКЦИОНИРРОВАНИЯ
    list_display = ['name', 'number']
admin.site.register(Category, CategoryAdmin)    
   
        
class Information_block_Admin(admin.ModelAdmin):    
    list_display = ['author', 'categories', 'topic', 'title', 'collection',# категории по списку предметов коллекционирования
    'text', 'in_publishid', 'time_publication', 'count_symbol_ok', 'count_symbol_bad', 
    'access',]                           
admin.site.register(Information_block, Information_block_Admin)
        
class Amalker_Admin(admin.ModelAdmin):
    list_display = ['name_seller', 'tabloid', 'time_publication', 'time_ending', 'categories', ]
admin.site.register(Amalker, Amalker_Admin)    
    
class ArticleCommentsAdmin(admin.ModelAdmin):  
    list_display = ['autor_publication', 'publication', 'time_publication', 'autor_message', 'text_message', 
    'count_symbol_bad', 'count_symbol_ok',]
admin.site.register(ArticleСomments, ArticleCommentsAdmin)    

class TopicInterestAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(TopicInterest, TopicInterestAdmin)   

# class  Article_commentsTwoAdmin(admin.ModelAdmin):
#      list_display = ['whom_message', 'time_publication', 'whose_message', 'text_message', 'count_symbol_ok', 'id_articl',
#     'count_symbol_bad','id_comment', 'write_author', 'access']
# admin.site.register(ArticleСommentsTwo) 

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
admin.site.register(Advertisement, AdvertisementAdmin)    

class CatalogyAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Catalogy, CatalogyAdmin)   

class AllowanceCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
admin.site.register(AllowanceComment, AllowanceCommentAdmin) 
