from django import forms 
from django.forms import ClearableFileInput
# from django.forms.forms import Form 


class NewArticleForm(forms.Form):
    title = forms.CharField(initial="название", max_length=150, ) 
    categories = forms.CharField(initial="по продукту",  max_length=150,) 
    topic = forms.CharField(initial="статья/продажа/покупка",  max_length=150,)
    text = forms.CharField( widget=forms.Textarea, initial="текст", ) 
    photo = forms.FileField(label='введите файл', initial="сюда:", widget = ClearableFileInput(attrs={'multiple': True}), )
    
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
