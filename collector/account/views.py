from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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

# Функция выхода из системы 
def logout_view(request):
    logout(request)
    context = {'a' : 'Вы вышли из системы'}
    return render(
        request,
        'account/logout.html',
        context)

# функция входа с паролем
def user_login(request):
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
                    user = authenticate(request,
                    username=us_name.username,
                    email=us_name.email,
                    password=password2)
                    # print(user)
                    # print('уже кое что3')
                    if user is not None:
                        # print('не активен')
                        # if user.is_active:
                        login(request, user)
                        print(login(request, user))
                        # return redirect('/account/confirmation/user={us_name.username}')
                        return redirect('/account/user={us_name.username}')         
                    else:
                        return HttpResponse('Неверно введен логин/пароль. Войдите через почту.')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(
        request,
        'account/login.html',
        context)

# функция входа на личную страницу пользователя
def personal_page(request, user): 
    
    context = {'form1':user}
    return render(request, 'account/individ_page.html', context)

# функция регистрации пользователя
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
                            user = authenticate(request,
                            username=j.username,
                            # email=us_name.email,
                            password=j.password)
                            if user is not None:
                                # print('не активен')
                                # if user.is_active:
                                login(request, user)
                            j.delete()
                            return redirect('/main/')
                    i.delete()
                    return redirect('/')
                    # return redirect('/main/')
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


# @login_required
# def personal_page (request, user_id=1):
#     print('lwerjngewgwertgtrwegtgn')  
#     return HttpResponse('<h1>%s</h1>' % user_id)

# функция отправки писем с токеном
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

# функция входа без пароля по почте с обновлением пароля поля
def login_email (request):
    print('1')
    user_email_autorise = ''
    text = 'Пожалуйста, введите вашу электронную почту:'
    password = 'ПОЛУЧИТЬ КЛЮЧ'
    if request.method == 'POST':
        print('2')
        form1 = LoginFormToken(request.POST) 
        form = LoginForm_Email(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            use_token = secrets.token_urlsafe()
            print(form['email_use'])
            print(use_token)
            print('3')
            user_tempory_key = UserTemporaryToken(username= form['email_use'], key_token = use_token)
            user_tempory_key.save()
            otpravka (form['email_use'], use_token, form['email_use'])
            print('4')
            open_file_bd(form['email_use'], use_token, form['email_use'])
            form1 = LoginFormToken()
            context2 = { 'form':form1,
                        'text1':'введите электронный ключ из письма с вашей почты',
                            'pasW' : 'Вход'}
            return render(request, 'account/login_email.html', context2)
        elif form1.is_valid():
            print('4')
            form1 = form1.cleaned_data
            for i in UserTemporaryToken.objects.all():
                print('5')
                # print(i)
                # print(form1['token_us'])
                # print(i.key_token)
                # print(i.username)
                if i.key_token == form1['token_us']:  
                    user_email = i.username
                    print(user_email)
                    print(6)
                    use = User.objects.get(email=user_email)
                    print(use.username)
                    print(use.email)
                    print(use)
                    use.set_password(form1['token_us'])
                    use.save()
                    use = authenticate(request,
                    username=use.username,
                    # email=us_name.email,
                    password=form1['token_us'])
                    if use is not None:
                        # print('не активен')
                        # if user.is_active:
                        login(request, use)
                    i.delete()
                    return redirect('/main/') # передалать на пользовательскую страницу
                else:
                    print('нет соответствия в цикле')
            else:           
                context = { 
                            'form':form,
                            'text1':'ключ введен не верно попробуйте пройти регистрацию заново',
                            'pasW' : 'Получить ключ'
                        } 
                return render(request, '/main/', context) 
    else:
        form = LoginForm_Email()
    context = {'form': form, 'text': text, 'pasW': password}
    return render(request, 'account/login_email.html', context)