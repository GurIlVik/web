from django.shortcuts import render
from django.http import HttpResponse


def privet(request):
    return render(
        request,
        'start/index.html',
        )



# def login(request):
#     return render(request, 'account/login.html')

    
