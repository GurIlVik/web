from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from sqlite3 import OperationalError


def function_show_article_2(dot, key_article, photo_clas, dict_draft):
    if dot:
        key_article = True  
        count = 0 
        list_draft = []
        for i in dot:
            # print(i)
            # print(i.pk)
            res = photo_clas.objects.filter(location__pk = i.pk) # запрос получения фотограпфий через id
            if res:
                for j in res:
                    list_draft.append(j.image)
                    count += 1
            else:
                list_draft.append(False)
            dict_photo = {count : list_draft}
            dict_draft[i] = dict_photo
            list_draft = []
            count = 0
    return key_article, dict_draft
            
# проверка 
def function_show_article(clas, photo_clas, filter_list = False):
    key_article = False                                                     # ключ статей
    dict_draft = {}
    if filter_list == False:
        try:
            dot = clas.objects.all()
        except OperationalError as error:
            print(error)
        else:
            key_article, dict_draft = function_show_article_2(dot, key_article, photo_clas, dict_draft)
    else:
        dot = []
        dot2 = []
        count = 0
        print('wlkfejbv')
        
        try:
            dot1 = clas.objects.all()
        except OperationalError as error:
            print(error)
        else:
            for i in dot1:
                for elem in filter_list:
                    if elem in i.collection and i not in dot:
                        count += 1
                        # print('zdec zikl')
                        # print(elem)
                        # print(i.collection)
                        # print(i)
                        # print(dot)
                        dot.append(i)
                        # print(dot)
        # print(dot)    
        # print('до функции')        
        if count!= 0: 
            key_article, dict_draft = function_show_article_2(dot, key_article, photo_clas, dict_draft)
    # print(key_article, dict_draft)
    return key_article, dict_draft 
        
# отображение главной страницы
def main_page(request):
    a = Catalogy.objects.all().order_by('name')  # сортировка списка по имени в базе
    b = ProstoList('prosto_list')
    c = Information_block.objects.all()
    e = Amalker.objects.all()
    predmet_collection_list = []   # В этом списке выбранные категории предметов
    g = chek_User_authenticated(request, 'Регистрация/ВХОД', 'ВЫХОД') # предоставление значений согласно логик
    h = chek_User_authenticated(request, "/", "/account/logout/")  # предоставление путей согласно логик
    j = f'/personalpage/{str(request.user)}'      # получение имени и питу на личную страницу
    # k = f'/personalpage/{str(request.user)}'
    
    key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock) 
    
    context = {
        'a': a,
        "form2" : b,
        'info_blok': dict_article,
        'key_article' : key_article,
        'amalker' : e,
        'log' : g,
        'puth_exit_enter' : h,
        'puth_paesonalpage' : j,
        'obchee' : Catalogy.objects.get(name='0'),
    }
    if request.method == 'POST':
        form = ProstoList(request.POST) 
        if form.is_valid(): 
            form = form.cleaned_data
            print(form)
            print('form')
            predmet_collection_list = method_main_page_1(form['pole']) # В этом списке выбранные категории предметов
            context['key_article'], context['info_blok'] = function_show_article(Information_block, PhotoInfoBlock, predmet_collection_list) 
            # context['info_blok'] = method_main_page_2(predmet_collection_list, c)
            # context['amalker'] = method_main_page_2(predmet_collection_list, e)
            # c = method_main_page_2(predmet_collection_list, c)
            # e = method_main_page_2(predmet_collection_list, e)
            print(predmet_collection_list)
            print(key_article)
            print(dict_article)
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


# отображение страницы публикации
def publication(request, author, id):
    c = Information_block.objects.filter(id = id)
    k = Information_block.objects.get(id = id)
    j = f'/personalpage/{str(request.user)}'
    form = CommemtUser()
    comm = ArticleComments.objects.filter(whom_message = k.id)
    form2 = CommentForComment()
    context = {'a' : author,
            'info_blok' : c, 
            'puth_paesonalpage' : j,
            'form' : form,
            'model' : comm,
            'form2' : form2,
            } 
    if request.method == 'POST':
        form = CommemtUser(request.POST)
        form2 = CommentForComment(request.POST)
        if form.is_valid(): 
            form = form.cleaned_data
            k = Information_block.objects.get(id = id)
            ArticleComments.objects.create(
                whom_message = k.id,                                        # ID статьи автора статьи
                whose_message = request.user,                               #  имя комментатора
                text_message = form['comment'],                                        #  текст комментария
                count_symbol_ok = 0,                                        # 
                count_symbol_bad = 0,  
                access = True     #
            )
            return render(request, 'main/publication.html', context)
        elif form2.is_valid(): 
            form2 = form2.cleaned_data
            print(form2)
            print(form2['comment2_id'])
            return render(request, 'main/publication.html', context)
        else:
            return HttpResponse('ЧТО_ТО ОПЯТЬ НЕ ТАК')
    else:
        print('без запроса')
        return render(request, 'main/publication.html', context)