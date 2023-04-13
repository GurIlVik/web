from django.contrib.auth.models import User
from django import forms
import secrets

from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError 
from django.forms.forms import Form 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya

class LoginForm(Form):
    username = forms.CharField(label='введите email или псевдоним')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput) 
 
class UserRegistrationForm(UserCreationForm):  
    username = forms.CharField(label='Придумайте псевдоним:', min_length=2, max_length=150) 
    email = forms.EmailField(label='Введите адрес электроной почты') 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput) 
    
    def username_clean(self):  
        username = self.cleaned_data['username']
        new = User.objects.filter(username = username) 
        if new.count(): 
            raise ValidationError("Такой псевдоним уже есть, выберете другой") 
        return username 
 
    def clean_email(self):  
        email = self.cleaned_data['email'].lower() 
        new = User.objects.filter(email=email) 
        if new.count(): 
            raise ValidationError("Пользователь с этой электронной почтой уже существует, войдите по почте") 
        return email
 
    def clean_password2(self): 
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
 
        if password1 and password2 and password1 != password2: 
            raise ValidationError("Пароль не совпадает") 
        return password2 
 
    def save(self, commit = True): 
        user = User.objects.create_user( 
            self.cleaned_data['username'], 
            self.cleaned_data['email'], 
            self.cleaned_data['password1'] 
        ) 
        return user 
    
class LoginForm_Email(Form):
    email_use = forms.EmailField(label='email') 
    
class LoginFormToken(Form):
    token_us = forms.CharField(label='ключ', min_length=20, max_length=150)


PASSWORD_EMAIL = 'hsphhbxdhczhzrhc'