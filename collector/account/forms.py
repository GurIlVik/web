from django.contrib.auth.models import User
from django import forms

from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError 
from django.forms.fields import EmailField 
from django.forms.forms import Form 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya

class LoginForm(Form):
    print('lwerjngelrjkgn')
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
   

# class UserRegistrationForm(forms.ModelForm):
class UserRegistrationForm(UserCreationForm):  
    print('lwerjngrfrjkgn')  
    username = forms.CharField(label='Пользователь', min_length=3, max_length=150) 
    email = EmailField(label='email') 
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput) 
 
    def username_clean(self): 
        print('lwerjngrfrjkgn1')  
        username = self.cleaned_data['username'].lower() 
        new = User.objects.filter(username = username) 
        if new.count(): 
            raise ValidationError("User Already Exist") 
        return username 
 
    def email_clean(self): 
        print('lwerjngrfrjkgn2')  
        email = self.cleaned_data['email'].lower() 
        new = User.objects.filter(email=email) 
        if new.count(): 
            raise ValidationError(" Email Already Exist") 
        return email 
 
    def clean_password2(self): 
        print('lwerjngrfrjkgn3')  
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 
 
        if password1 and password2 and password1 != password2: 
            raise ValidationError("Password don't match") 
        return password2 
 
    def save(self, commit = True): 
        print('lwerjngrfrjkgn4') 
        user = User.objects.create_user( 
            self.cleaned_data['username'], 
            self.cleaned_data['email'], 
            self.cleaned_data['password1'] 
        ) 
        print('lwerjngrfrjkgn5') 
        return user 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya
    
    
    
    
    
    
    
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



