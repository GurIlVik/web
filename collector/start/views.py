from django.shortcuts import render
from django.http import HttpResponse
# from personalpage.views import getting_nickname_request
# from django.contrib.auth.models import User


def privet(request):
    req = request.user
    print(req)
    context = {
        'puth_paesonalpage' : req, 
    }
    return render(
        request,
        'start/index.html', 
        context
        )


 
