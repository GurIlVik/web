from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Information_block, Article_comments, Amalker
from .forms import ProstoList


def main_page(request):
    a = Category.objects.all().order_by('name')  # сортировка списка по имени в базе
    b = ProstoList('prosto list')
    c = Information_block.objects.all()
    predmet_collection_list = []   # В этом списке выбранные категории предметов
    context = {
        'a': a,
        "form2" : b,
        'info_blok': c,
    }
    if request.method == 'POST':
        form = ProstoList(request.POST) 
        if form.is_valid(): 
            form = form.cleaned_data
            predmet_collection_list = motod_main_page_1(form['pole'])
            print(predmet_collection_list)
        return render(request, 'main/index.html', context)
    
    return render(request, 'main/index.html', context)
    
    
# Вспомогательная функция сортировки коллекционных предметов пришедших с формы после JScript
def motod_main_page_1(a):
    list_a = []
    str_a = ''
    for i in range(len(a)):
        if a[i] == ',':
            list_a.append(str_a)
            str_a = ''
        elif a[i] == " " and a[i-1] == ',':
                pass
        else:
            str_a += a[i]
    return list_a

