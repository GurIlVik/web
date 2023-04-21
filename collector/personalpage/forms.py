from django import forms 
from django.forms import ClearableFileInput, ModelForm, TextInput
from main.models import Category, Catalogy, AllowanceComment
from .models import PresentationUser, AllowanceModel, InfoUser, Professional
from multiupload.fields import MultiFileField

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
    photo = MultiFileField(min_num=0, max_num=5,required=False )
#     photo = forms.ImageField(label=u'введите файл', 
#             widget=forms.FileInput(attrs={'multiple': 'multiple'}), required=False)
    
#     photo = forms.ImageField(label='введите файл', 
#             widget = ClearableFileInput(attrs={'multiple': True, 'class': 'main_form_text'}), 
#             )

class AllowanceForm(forms.ModelForm):
    class Meta:
        model = AllowanceModel
        fields = ['for_page', 'for_inform', 'for_messeng']     

class SpecialInfoUser(forms.ModelForm):
     class Meta:
        model = InfoUser
        fields = ['name', 'name_last', 'name_first', 'telephon']   
        
        
class PersonalInformationUser(forms.Form):
    
    interest = forms.CharField(max_length=150,)
    profession = forms.ModelChoiceField(                                                   # категория
            queryset=Professional.objects.all().order_by('name'),
            label='Род деятельности',
            empty_label = 'К выбору обязателен',
            # widget=forms.TextInput(attrs={'class': 'main_form_categories'}),
            )  
    
    photo = forms.ImageField(label='введите файл',                                       # загрузка файлов
            )