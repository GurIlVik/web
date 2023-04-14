from django import forms 
from django.forms import ClearableFileInput
from main.models import Category, Catalogy, AllowanceComment
from .models import PresentationUser

class NewArticleForm(forms.Form):
    title = forms.CharField(
        #     initial="название", 
                            max_length=150,                            # название статьи
            widget=forms.TextInput(attrs={'class': 'main_form_title'})) 
    categories = forms.ModelChoiceField(                                                   # категория
            queryset=Category.objects.all().order_by('name'),
            label='Категория статьи',
            empty_label = 'К выбору обязателен',
            # widget=forms.TextInput(attrs={'class': 'main_form_categories'}),
            )  
    topic = forms.ModelChoiceField(                                                        # каталог
            queryset=Catalogy.objects.all().order_by('name'),
            label='Предмет коллекционирования',
            empty_label = 'К выбору обязателен',
            )
    
    text = forms.CharField( widget=forms.Textarea, 
                        #    initial="текст",                        # текст сообщения
            ) 
    allowance = forms.ModelChoiceField(                                                        # каталог
            queryset=AllowanceComment.objects.all().order_by('name'),
            label='',
            empty_label = 'К выбору обязателен',
            )
    
    photo = forms.FileField(label='введите файл',                                          # загрузка файлов
            initial="сюда:", 
            widget = ClearableFileInput(attrs={'multiple': True, 'class': 'main_form_text'}), 
            )
    
    
# class Draft(forms.Form):
#     title = forms.CharField(initial="название", max_length=150,                            # название статьи
#             widget=forms.TextInput(attrs={'class': 'main_form_title'})) 
#     text = forms.CharField( widget=forms.Textarea, initial="текст",                        # текст сообщения
#             ) 
#     photo = forms.FileField(label='введите файл',                                          # загрузка файлов
#             initial="сюда:", 
#             widget = ClearableFileInput(attrs={'multiple': True, 'class': 'main_form_text'}), 
#             )

class PersonalInformationUser(forms.ModelForm):
    class Meta:
        model = PresentationUser
        fields = '__all__'
        # fields = ['photo', "profession", 'interest']
        