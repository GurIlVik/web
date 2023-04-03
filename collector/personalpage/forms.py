from django import forms 
from django.forms import ClearableFileInput
from django.forms.forms import Form 


class NewArticleForm(Form):
    title = forms.CharField(initial="название", ) 
    # title = forms.CharField(label='название') 
    text = forms.CharField( widget=forms.Textarea, initial="текст") 
    photo = forms.FileField(label='введите файл', initial="сюда:", widget = ClearableFileInput(attrs={'multiple': True}))
    
    # class Meta:
    #     widgets = {
    #         'photo': ClearableFileInput(attrs={'multiple': True})
    #     }
    
# class NewArticleForm(Form):
#     class Meta:
#         model = NewArticle
#         fields = '__all__'
#         widgets = {
#             'photo': ClearableFileInput(attrs={'multiple': True})
#         }
