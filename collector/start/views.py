from django.shortcuts import render

def privet(request):
    return render(
        request,
        'start/index.html',
        )
    
