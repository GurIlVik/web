from django.contrib.auth.models import User
from django import forms
import secrets


from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError 
from django.forms.fields import EmailField 
from django.forms.forms import Form 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya

class LoginForm(Form):
    username = EmailField(label='email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput) 
   
# class UserRegistrationForm(forms.ModelForm):
class UserRegistrationForm(UserCreationForm):  
    username = EmailField(label='email') 
    username2 = forms.CharField(label='Пользователь', min_length=3, max_length=150) 
    # email = EmailField(label='email') 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput) 
    
    def username_clean(self):  
        username = self.cleaned_data['username'].lower() 
        new = User.objects.filter(username = username) 
        if new.count(): 
            raise ValidationError("Пользователь уже существует") 
        return username 
 
    def username2_clean(self):  
        username2 = self.cleaned_data['username2'].lower() 
        new = User.objects.filter(username2=username2) 
        if new.count(): 
            raise ValidationError("Электронная почта уже существует, войдите по почте") 
        return username2 
 
    def clean_password2(self): 
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
 
        if password1 and password2 and password1 != password2: 
            raise ValidationError("Пароль не совпадает") 
        return password2 
 
    def save(self, commit = True): 
        user = User.objects.create_user( 
            self.cleaned_data['username'], 
            self.cleaned_data['username2'], 
            self.cleaned_data['password1'] 
        ) 
        print('lwerjngrfrjkgn5') 
        return user 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya
    
class LoginForm_Email(Form):
    email_use = EmailField(label='email') 
    # token_us = forms.CharField(label='ключ', min_length=20, max_length=150)
    # email = forms.CharField(label='email')

    
class LoginFormToken(Form):
    token_us = forms.CharField(label='ключ', min_length=20, max_length=150)
    
    

      
    
    
    
    
    
    # useremail = forms.EmailField(
    #     label = "Введите email"
    # )
    # password = forms.CharField(
    #     label='Пароль',
    #     widget=forms.PasswordInput)
    # password2 = forms.CharField(
    #     label='Повтор Пароля',
    #     widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = (
    #         'username',)
            # 'first_name',
            # 'email',)

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError(
    #             'Passwords don\'t match.')
    #     return cd['password2'] 



