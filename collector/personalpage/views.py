from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm, UserRegistrationForm, LoginForm_Email, LoginFormToken
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import urls
# from .models import UserTemporaryModels, UserTemporaryToken

@ login_required
def personal_page(request, user): 
    print(user)
    
    a = False
    context = {'form' : a}

    for us in User.objects.all():
        if user == us.username:
            print(us.username)   
            a= True
            
            return render(request, 'personalpage/index.html', context)
        
    return HttpResponse('такого пользователя нет')