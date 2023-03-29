from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from .forms import LoginForm, UserRegistrationForm, LoginForm_Email, LoginFormToken
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# from .models import UserTemporaryModels, UserTemporaryToken


def personal_page(request, user): 
    context = {'form1': user}
    return render(request, 'personalpage/index.html', context)