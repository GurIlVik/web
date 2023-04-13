from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# from personalpage.views import getting_nickname_request
# from django.contrib.auth.models import User


def privet(request):
    req = request.user
    title = 'Приветствие'
    print(req)
    context = {
        'puth_paesonalpage' : req, 
        'title' : title,
    }
    return render(
        request,
        'start/index.html', 
        context
        )

def page_not_found(request, exception):
    return HttpResponseNotFound('Что-то пошло не так')
 
