from django import forms 
from django.forms import ClearableFileInput
from main.models import Category, Allowance
# from django.forms.forms import Form 


class NewArticleForm(forms.Form):
    title = forms.CharField(initial="название", max_length=150,                            # название статьи
            widget=forms.TextInput(attrs={'class': 'main_form_title'})) 
    categories = forms.ModelChoiceField(                                                   # предмет коллекционирования
            queryset=Category.objects.all().order_by('name'),
            label='Предмет коллекционирования',
            empty_label = 'К выбору обязателен',
            # widget=forms.TextInput(attrs={'class': 'main_form_categories'}),
            )  
    topic = forms.CharField(initial="статья/продажа/покупка",  max_length=150,             # категория сообщения 
            widget=forms.TextInput(attrs={'class': 'main_form_topic'}))
    text = forms.CharField( widget=forms.Textarea, initial="текст",                        # текст сообщения
            ) 
    allowance = forms.CharField(initial="допуск", max_length=50,                            # допуск к статьи
        #     queryset=Allowance.objects.all().order_by('name'),
            )
    
    photo = forms.FileField(label='введите файл',                                          # загрузка файлов
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
