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

class  Article_commentsTwoAdmin(admin.ModelAdmin):
     list_display = ['author_comment', 'comment', 'time_publication', 'text_message', 'count_symbol_ok', 'author_re_comment',
    'count_symbol_bad',]
admin.site.register(ArticleСommentsTwo) 

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
admin.site.register(Advertisement, AdvertisementAdmin)    

class CatalogyAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Catalogy, CatalogyAdmin)   

class AllowanceCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
admin.site.register(AllowanceComment, AllowanceCommentAdmin) 

class CountArticleAdmin(admin.ModelAdmin):
    list_display = ['author_count', 'article_count', 'count_simbol', 'simbol']
admin.site.register(CountArticle, CountArticleAdmin)

class CountCommentAdmin(admin.ModelAdmin):
    list_display = ['author_count', 'article_count', 'count_simbol', 'simbol']
admin.site.register(CountComment, CountCommentAdmin)

class CountComment2Admin(admin.ModelAdmin):
    list_display = ['author_count', 'article_count', 'count_simbol', 'simbol']
admin.site.register(CountComment2, CountComment2Admin)

class LetterAuthorAdmin(admin.ModelAdmin):
    list_display = ['correspondent', 'article', 'auhtor', 'text']
admin.site.register(LetterAuthor, LetterAuthorAdmin)