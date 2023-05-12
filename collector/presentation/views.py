from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from personalpage.models import PresentationUser

# отображение главной страницы
def index_1(request):
    context = {'word1' : 'сайт коллекционер'}
    return render(request, 'presentation/index_1.html', context)