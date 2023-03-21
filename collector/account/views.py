from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, LoginForm_Email, LoginFormToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import secrets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .sekret import password
from .models import UserTemporaryModels, UserTemporaryToken
from .datebase import open_file_bd

def user_login(request):
    # print('wergfqfgqerngrfrjkgn')  
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pole1 = cd['username']
            password2 = cd['password']
            # print(pole1)
            # print(password2)
            for us_name in User.objects.all():
                # print('уже кое что')
                if pole1 == us_name.username or pole1 == us_name.email:
                    # print('уже кое что2')
                    user = authenticate(
                    username=us_name.username,
                    # email=us_name.email,
                    password=password2)
                    # print(user)
                    # print('уже кое что3')
                    if user is None:
                        # print('не активен')
                        # if user.is_active:
                        login(request, user)
                        print(login(request, user))
                        return redirect('/main/')         
                    else:
                        return HttpResponse('Неверно введен логин/пароль. Войдите через почту.')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(
        request,
        'account/login.html',
        context)

from django.contrib.auth.models import User

def confirmation(request, email, user2):
    print(1)
    d = UserTemporaryModels.objects.all()
    print(d)
    k = type(UserTemporaryModels)
    print(k)
    for i in d:
        print(2)
        if i.email == email[6::]:
            print(3)
            d = i.password
            
            user = User.objects.create_user( 
                    user2[6::], 
                    email[6::], 
                    d
                )
            context = {'form1':user2}
            return render(request, 'account/confirmation.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        form2 = LoginFormToken(request.POST) 
        if form.is_valid(): 
            form = form.cleaned_data
            use_token = secrets.token_urlsafe()
            user_tempory = UserTemporaryModels(email = form['email'], 
                                               username= form['username'], 
                                               password = form['password1'], 
                                               password2 = form['password2'],
                                               
                                               )
            user_tempory_key = UserTemporaryToken(username= form['username'], key_token = use_token)
            user_tempory.save() 
            user_tempory_key.save()
            otpravka (form['email'], use_token, form['username'])
            open_file_bd(form['email'], use_token, form['username'])
            form2 = LoginFormToken()
            context2 = { 'form':form2,
                        'text1':'введите электронный ключ из письма с вашей почты'}
            return render(request, 'account/register.html', context2)
        elif form2.is_valid(): 
            form2 = form2.cleaned_data
            for i in UserTemporaryToken.objects.all():
                if i.key_token == form2['token_us']:
                    for j in UserTemporaryModels.objects.all():
                        if i.username == j.username:
                            user = User.objects.create_user( 
                                j.username, 
                                j.email, 
                                j.password
                            )
                            j.delete()
                    i.delete()
                    return redirect('/')
                else:
                    print(i.username)
                    print(i.key_token)
            else:           
                context = { 
                            'form':form,
                            'text1':'ключ введен не верно попробуйте пройти регистрацию заново'
                        } 
                return render(request, 'account/register.html', context) 
    else: 
        form = UserRegistrationForm() 
    context = { 
        'form':form,
        'text1':'Заполните форму регистрации'
    } 
    return render(request, 'account/register.html', context) 

@login_required
def personal_page (request, user_id=1):
    print('lwerjngewgwertgtrwegtgn')  
    return HttpResponse('<h1>%s</h1>' % user_id)

def otpravka (email_user, token_user, username2,):
        my_mail = 'forsitecollector@yandex.ru' # твоя почта с которой будешь отправлять письмо
        msg = MIMEMultipart()
        msg['From'] = my_mail  
        msg['To'] = email_user 
        msg['Subject'] = 'скопируйте ключ и вставьте в форму на сайте' # пишешь тему письма
        #message = f'Внизу код который необходимо ввести на сайте: \n \n \n{token_user}'
        # message = f'Пройдите по ссылке для завершения регистрации: \n \n http://127.0.0.1:8000/account/confirmation/email={email_user}/token={token_user}'
        # message = f"""Пройдите по ссылке для завершения регистрации: \n \n 
        #                 http://127.0.0.1:8000/account/confirmation/email={email_user}/user2={username2} \n \n
        #                 и введите ключ: \n \n {token_user}"""
                        # http://127.0.0.1:8000/account/confirmation/email={email_user} \n \n
        # message = token_user
        # print(message)
        # msg.attach(MIMEText(message))
        msg.attach(MIMEText(token_user))
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

def login_email (request):
    user_email_autorise = ''
    text = 'Пожалуйста, введите вашу электронную почту:'
    password = 'ПОЛУЧИТЬ КЛЮЧ'
    if request.method == 'POST':
        form = LoginForm_Email(request.POST)
        if form.is_valid():
            email_user = form.cleaned_data 
            user_email_autorise = email_user['email_use'].lower() 
            n = 0
            print('ljwefbgoiuerjbnvoierjbnoigrbe')
            if n < 1:
                KEY_TOKEN = secrets.token_urlsafe()
                key_token = KEY_TOKEN
                otpravka(user_email_autorise, key_token)
                n +=1
            text = 'Пожалуйста, введите ключ с вашей электронной почты:'
            password = 'ВХОД'
            form1 = LoginFormToken(request.POST)
            if form1.is_valid():
                print('сюда попаcть труд')
                token_of_user = form1.cleaned_data
                token_of_user = token_of_user['token_us']
                key_token = KEY_TOKEN
                print(token_of_user)
                print(key_token)
                if key_token == key_token: # подделка из-за нерешенной второй отправки
                    print('check')
                    user = authenticate(
                       useremail=user_email_autorise)
                    print(user)
                    print(type(user))
                    if user.is_active:
                        print('check3')
                        login(request, user)
                        print('check4')
                        return HttpResponse('Успешно')
                    else:
                        return HttpResponse('Аккаунт заблокирован')
                else:
                    text = 'Ключ не соответствует почте:'
                    
                    
                
               
    else:
        form = LoginForm_Email()
        form1 = None
    return render(
        request,
        'account/login_email.html',
        {'form': form, 'form1': form1, 'text': text, 'pasW': password})