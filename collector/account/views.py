from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, LoginForm_Email, LoginFormToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import secrets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .sekret import password

def user_login(request):
    print('wergfqfgqerngrfrjkgn')  
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                       username=cd['username'],
                       password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешно')
                else:
                    return HttpResponse('Аккаунт заблокирован')
            else:
                return HttpResponse('Неверно введен логин/пароль. Войдите через почту.')
    else:
        form = LoginForm()
    return render(
        request,
        'account/login.html',
        {'form': form})
    
def register(request):
    # form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        print('lwerjngrfrjkgn34')  
        if form.is_valid(): 
            print('lwerjngrfrjkgn45')  
            form.save() 
    else: 
        form = UserRegistrationForm() 
    context = { 
        'form':form 
    } 
    return render(request, 'account/register.html', context) 

@login_required
def personal_page (request, user_id=1):
    print('lwerjngewgwertgtrwegtgn')  
    return HttpResponse('<h1>%s</h1>' % user_id)

def login_email (request):
    
    def otpravka (email_user, token_user):
        my_mail = 'forsitecollector@yandex.ru' # твоя почта с которой будешь отправлять письмо
        user_email = email_user # вводишь почту кому будешь отправлять письмо

        msg = MIMEMultipart()
        msg['From'] = my_mail  
        msg['To'] = email_user 
        msg['Subject'] = 'письмо с паролем для входа на сайт' # пишешь тему письма
        message = f'Внизу код который необходимо ввести на сайте: \n {token_user}'
        msg.attach(MIMEText(message))
        try:
            mailserver = smtplib.SMTP('smtp.yandex.ru',587)
            mailserver.set_debuglevel(True)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login(my_mail, password) # твоя почта и пароль с которого бутет отправка письма
            mailserver.sendmail(my_mail, email_user, msg.as_string()) # первое твоя почта далее почта получателя
            mailserver.quit()
            print("Письмо успешно отправлено")
        except smtplib.SMTPException:
            print("что то пошло не так ((")
    
    
    print('wergfqfgqerngrfrjkgn')  
    if request.method == 'POST':
        key_token = secrets.token_urlsafe()
        email_user = LoginForm_Email(request.POST)
        if email_user != '':
            otpravka(email_user, key_token)
            token_user = LoginFormToken(request.POST)
            if key_token == token_user:
                user = authenticate(
                    username=cd['username'],
                    password=cd['password'])
            
            
           
            user = authenticate(
                       username=cd['username'],
                       password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешно')
                else:
                    return HttpResponse('Аккаунт заблокирован')
            else:
                return HttpResponse('Неверно введен логин/пароль. Войдите через почту.')
    else:
        form = LoginForm_Email()
    return render(
        request,
        'account/login_email.html',
        {'form': form})
    
    
    # print('23')  
    # form = None
    # key_token = secrets.token_urlsafe()
    # if request.method == 'POST':
    #     form = LoginForm_Email.email(request.POST)
    #     if form.email_clean(form):
    #         return key_token
    # else:
    #     form = LoginForm_Email()    
        
    # return render(
    #     request,
    #     'account/login-email.html',
    #     {'form': form})
    
    
    
    
    
    
    
    
    
# class LoginForm_Email(Form):
#     print('456')
#     email = EmailField(label='email') 
#     token_us = forms.CharField(label='ключ', min_length=20, max_length=150)
    
#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower() 
#         new = User.objects.filter(email=email) 
#         if new.count():
#             return email
#         else: 
#             raise ValidationError("Электронная почта уже существует, войдите по почте") 
    
    
    
    
    
    # return HttpResponse(key_token)


# from django.contrib.auth import forms 
# from django.shortcuts import redirect, render 
# from django.contrib import messages 
# from django.contrib.auth.forms import UserCreationForm 
# # from .forms import CustomUserCreationForm 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya
    #     user_form = UserRegistrationForm(request.POST)
    #     if user_form.is_valid():
    #         new_user = user_form.save(commit=False)
    #         new_user.set_password(user_form.cleaned_data['password'])
    #         new_user.save()
    #         return render(request, 'account/register_done.html', {'new_user': new_user})
    # else:
    #     user_form = UserRegistrationForm()
    # return render(
    #     request,
    #     'account/register.html',
    #     {'form': user_form},
    #     # {'user_form': user_form},
    #     )
    