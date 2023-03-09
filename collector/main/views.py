from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def main_page(request):
    a = Category.objects.all()
    # a = Category.objects.extra(select={'field': 'SELECT name FROM core_page ORDER BY name ASC limit 1'})
    context = {
        'a': a
    }
    return render(
        request,
        'main/index.html', context
        )