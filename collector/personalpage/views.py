from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm, UserRegistrationForm, LoginForm_Email, LoginFormToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import urls
from main.models import Information_block
# from .models import UserTemporaryModels, UserTemporaryToken

@ login_required
def personal_page(request, user): 
    nik_reguest = getting_nickname_request(request)  # получение имени пришедшего пользователя
    search_user = user_page_search(user)  # получение булевого есть ли такой пользователь (тру/фальш)
    registered_user = chek_user_register(request)  # логик тру пользователь зарегистрирован или нет фальш
    print(user)             # имя страницы пользователя
    print(nik_reguest)      # имя зашедшего на страницу
    print(search_user)      # тру-страница есть фальш - страницы нет
    print(registered_user)  # тру-зарегистрирован | нет фальш
    a = Information_block.objects.all()
    if search_user:
        password = chek_user_access(user, nik_reguest) # логик - тру страница индивида или нет фальш
        context = {'nik_name' : nik_reguest,
                   'access' : password,
                   'register' : registered_user,
                   'information_block' : a,}
        return render(request, 'personalpage/index.html', context)
        
    return HttpResponse('такого пользователя нет')


# Функция получения имени пользователя из запроса 
def getting_nickname_request(request):
    as_us = str(User.objects.filter(username=request.user))
    as_us = as_us[18:]
    return as_us[:-3]

# функция проверки наличия страницы пользователя
def user_page_search(user):
    for us in User.objects.all():
        if user == us.username:
            return True
    return False

# функция получения логики (страница ли пользователя)
def chek_user_access(user, nik_reguest):
    if user == nik_reguest:
        return True
    return False

# логика зарегистрированость пользователя
def chek_user_register(request):
    if request.user.is_authenticated:
        return True
    return False
    