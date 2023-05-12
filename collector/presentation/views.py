from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from personalpage.models import PresentationUser

# отображение главной страницы
def index_1(request):
    context = {'word1' : 'Клюб коллекционеров'}
    return render(request, 'presentation/index_1.html', context)

def index_2(request):
    context = {'word1' : 'Клюб коллекционеров'}
    return render(request, 'presentation/index_2.html', context)

def index_3(request):
    context = {'word1' : 'Клюб коллекционеров'}
    return render(request, 'presentation/index_3.html', context)

def index_4(request):
    context = {'word1' : 'Клюб коллекционеров'}
    return render(request, 'presentation/index_4.html', context)

def index_5(request):
    context = {'word1' : 'Клюб коллекционеров'}
    return render(request, 'presentation/index_5.html', context)