from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import forms 
from django.shortcuts import redirect, render 
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm 
# from .forms import CustomUserCreationForm 
# Источник: https://pythonpip.ru/django/django-usercreationform-sozdanie-novogo-polzovatelya

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
                return HttpResponse('Неверно введен логин/пароль')
    else:
        form = LoginForm()
    return render(
        request,
        'account/login.html',
        {'form': form})
    
def register(request):
    form = UserRegistrationForm()
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
    
    
    

@login_required
def personal_page (request, user_id=1):
    print('lwerjngewgwertgtrwegtgn')  
    return HttpResponse('<h1>%s</h1>' % user_id)

def login_email (request):
    print('lewgwergtwgrtwgertewfgwregfrjkgn')  
    return HttpResponse('<h1>В стадии разработки</h1>')
