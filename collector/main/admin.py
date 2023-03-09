from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('title', 'author', 'price')
#admin.site.register(Book, BookAdmin)
    list_display = ['name']#Category._meta.get_all_field_names()
    #class meta:
        #list_display = ['name']#Category._meta.get_all_field_names()


admin.site.register(Category, CategoryAdmin)