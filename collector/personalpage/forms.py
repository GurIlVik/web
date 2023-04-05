from django import forms 
from django.forms import ClearableFileInput
from main.models import Category
# from django.forms.forms import Form 


class NewArticleForm(forms.Form):
    title = forms.CharField(initial="название", max_length=150, 
            widget=forms.TextInput(attrs={'class': 'main_form_title'})) 
    categories = forms.ModelChoiceField( 
            queryset=Category.objects.all().order_by('name'),
            label='Предмет коллекционирования',
            empty_label = 'К выбору обязателен',
            # widget=forms.TextInput(attrs={'class': 'main_form_categories'}),
            )  
    topic = forms.CharField(initial="статья/продажа/покупка",  max_length=150,
            widget=forms.TextInput(attrs={'class': 'main_form_topic'}))
    text = forms.CharField( widget=forms.Textarea, initial="текст", 
            ) 
    photo = forms.FileField(label='введите файл', 
            initial="сюда:", 
            widget = ClearableFileInput(attrs={'multiple': True, 'class': 'main_form_text'}), 
            )
    
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
