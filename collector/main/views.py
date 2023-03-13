from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.
def main_page(request):
    # a = Category.objects.all()
    a = Category.objects.all().order_by("name")  # сортировка списка
    context = {
        'a': a
    }
    return render(
        request,
        'main/index.html', context
        )