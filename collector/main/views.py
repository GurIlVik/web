from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Information_block, Article_comments, Amalker
from .forms import ProstoList


        

def main_page(request):
    a = Category.objects.all().order_by('name')  # сортировка списка по имени в базе
    b = ProstoList('prosto list')
    c = Information_block.objects.all()
    e = Amalker.objects.all()
    predmet_collection_list = []   # В этом списке выбранные категории предметов
    g = chek_User_authenticated(request, 'Регистрация/ВХОД', 'ВЫХОД') # предоставление значений согласно логик
    h = chek_User_authenticated(request, "/", "/account/logout/")  # предоставление путей согласно логик
    j = f'/personalpage/{str(request.user)}'      # получение имени и питу на личную страницу
    context = {
        'a': a,
        "form2" : b,
        'info_blok': c,
        'amalker' : e,
        'log' : g,
        'puth_exit_enter' : h,
        'puth_paesonalpage' : j,
    }
    if request.method == 'POST':
        form = ProstoList(request.POST) 
        if form.is_valid(): 
            form = form.cleaned_data
            predmet_collection_list = method_main_page_1(form['pole']) # В этом списке выбранные категории предметов
            context['info_blok'] = method_main_page_2(predmet_collection_list, c)
            context['amalker'] = method_main_page_2(predmet_collection_list, e)
            c = method_main_page_2(predmet_collection_list, c)
            e = method_main_page_2(predmet_collection_list, e)
            return render(request, 'main/index.html', context)
        return render(request, 'main/index.html', context)
    
    return render(request, 'main/index.html', context)
     
# Вспомогательная функция сортировки коллекционных предметов пришедших с формы после JScript
def method_main_page_1(a):
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

# вспомогательная функция смены 
def method_main_page_2(a, b):
    s = []
    for elem in a:
        for elem2 in b:
            if elem in elem2.categories:
                if elem2 not in s:
                    s.append(elem2)
    return s


# функция проеверки пользователя на аутентификацию с запросом
def chek_User_authenticated(request, a = None, b = None):
    if request.user.is_authenticated:
        a = b
    return a