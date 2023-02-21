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

from django.contrib.auth.models import User

def confirmation(request, email, token):
    print(email, token)
    user = User.objects.create_user( 
            email, 
            'kuku 1', 
            'jjjjkkkk' 
        )
    HttpResponse('Ok')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST) 
        #if form.is_valid(): 
        otpravka (form['username'], 'lll')
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

def otpravka (email_user, token_user):
        my_mail = 'forsitecollector@yandex.ru' # твоя почта с которой будешь отправлять письмо
        msg = MIMEMultipart()
        msg['From'] = my_mail  
        msg['To'] = email_user 
        msg['Subject'] = 'письмо с паролем для входа на сайт' # пишешь тему письма
        #message = f'Внизу код который необходимо ввести на сайте: \n \n \n{token_user}'
        message = f'Пройдите по ссылке для завершения регистрации: \n \n http://127.0.0.1:8000/account/confirmation/email={email_user}/token={token_user}'
        print(message)
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

KEY_TOKEN = ''

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
