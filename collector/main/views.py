from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
# from .forms import Collectible_for_user
# from html.parser import HTMLParser
# from html.entities import *
from .forms import ProstoList

# Create your views here.
def main_page(request):
    a = Category.objects.all().order_by('name')  # сортировка списка по имени в базе
    b = ProstoList('prosto list')

    print('form')
    if request.method == 'POST':
        form = ProstoList(request.POST) 
        #print(form)
        print(request.POST) 
        if form.is_valid(): 
            #form = form.cleaned_data
            print(form)#.cleaned_data)
            #for i in form:
            #    return HttpResponse('i')
    context = {
        'a': a,
        "form2" : b
    }
    return render(
        request,
        'main/index.html', context
        )

























# Create your views here.
# def main_page(request):
    
#     # a = Category.objects.all()
#     a = Category.objects.all().order_by("name")  # сортировка списка
#     if request.method == 'POST':
        
#         re.findall(r'<body.*?>(.*)</body>', text, re.DOTALL)
#         print(text)
#     context = {
#         'a': a,
#         # 'form' : form,
#     }
#     return render(
#         request,
#         'main/index.html', context
#         )