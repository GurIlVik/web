from django.contrib import admin
from .models import Category, Information_block, Article_comments, Amalker, TopicInterest, Article_commentsTwo


class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author', 'price')
#admin.site.register(Book, BookAdmin)
    list_display = ['name']#Category._meta.get_all_field_names()
admin.site.register(Category, CategoryAdmin)    
    #class meta:
        #list_display = ['name']#Category._meta.get_all_field_names()
        
class Information_block_Admin(admin.ModelAdmin):    
    list_display = ['picture_author', 'page_author', 'time_publication', 'categories', # категории по списку предметов коллекционирования
    'topic_interest', 'table_contents', 'text_contents', 'symbol_ok', 'count_symbol_ok', 'symbol_bad', 'count_symbol_bad', 'comment_article',
    'write_author', 'access',]                           
admin.site.register(Information_block, Information_block_Admin)
        
class Amalker_Admin(admin.ModelAdmin):
    list_display = ['name_seller', 'tabloid', 'time_publication', 'time_ending', 'categories', ]
admin.site.register(Amalker, Amalker_Admin)    
    
class Article_comments_Admin(admin.ModelAdmin):  
    list_display = ['whom_message', 'time_publication', 'whose_message', 'text_message', 'count_symbol_ok', 'symbol_bad',
    'count_symbol_bad','comment_article', 'write_author',]
admin.site.register(Article_comments, Article_comments_Admin)    


class TopicInterestAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(TopicInterest, TopicInterestAdmin)   

class  Article_commentsTwoAdmin(admin.ModelAdmin):
     list_display = ['whom_message', 'time_publication', 'whose_message', 'text_message', 'count_symbol_ok', 'id_articl',
    'count_symbol_bad','id_comment', 'write_author', 'access']
admin.site.register(Article_commentsTwo, Article_commentsTwoAdmin) 