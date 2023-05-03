from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from sqlite3 import OperationalError
from django.contrib.auth.models import User
from personalpage.models import PresentationUser


# отображение главной страницы
def main_page(request):
    list_interest = PresentationUser.objects.get(user=request.user).interest
    a = Catalogy.objects.all().order_by('name')  # сортировка списка по имени в базе
    b = ProstoList('prosto_list')
    c = Information_block.objects.all()
    e = Amalker.objects.all()
    predmet_collection_list = []   # В этом списке выбранные категории предметов
    g = chek_User_authenticated(request, 'Регистрация/ВХОД', 'ВЫХОД') # предоставление значений согласно логик
    h = chek_User_authenticated(request, "/", "/logout/")  # предоставление путей согласно логик
    j = f'/personalpage/{str(request.user)}'      # получение имени и питу на личную страницу
    
    list_interest = list_interest_user(list_interest)
    key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock) 
    if list_interest:
        key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock, filter_list = list_interest) 
        
    print(key_article)
    print(dict_article)
    
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
            predmet_collection_list = method_main_page_1(form['pole']) # В этом списке выбранные категории предметов
            context['key_article'], context['info_blok'] = function_show_article(Information_block, PhotoInfoBlock, filter_list = predmet_collection_list) 
            return render(request, 'main/index.html', context)
        return render(request, 'main/index.html', context)
    
    return render(request, 'main/index.html', context)
     
def function_show_comments(param, key):
    key_article = False                                                     # ключ статей
    list_draft = []
    dot = ''
    try:
        dot = param.objects.filter()
    except OperationalError as error:
        print('ошибочка')
    else:
        key_article = True
        print(dot)
        if dot:
            for i in dot:
                list_draft. append(i)
    return key_article, list_draft
    

# отображение страницы публикации
def publication(request, author, id):
    c = Information_block.objects.filter(id = id)
    k = Information_block.objects.get(id = id)
    j = f'/personalpage/{str(request.user)}'
    form = CommemtUser()
    # comm = ArticleСomments.objects.filter(publication = k.pk)
    form2 = CommentForComment()
    print(k)
    print(k.pk)
    # print(comm)
    key_comments, dict_comments = function_show_comments(ArticleСomments, k.pk)
    
    context = {'a' : author,
            'info_blok' : c, 
            'puth_paesonalpage' : j,
            'form' : form,
            'key_comments' : key_comments,
            'dict_comments' : dict_comments,
            'model' : dict_comments,
            'form2' : form2,
            } 
    if request.method == 'POST':
        form = CommemtUser(request.POST)
        form2 = CommentForComment(request.POST)
        if form.is_valid(): 
            form = form.cleaned_data
            k = Information_block.objects.get(id = id)
            # ArticleComments.objects.create(
            #     whom_message = k.id,                                        # ID статьи автора статьи
            #     whose_message = request.user,                               #  имя комментатора
            #     text_message = form['comment'],                                        #  текст комментария
            #     count_symbol_ok = 0,                                        # 
            #     count_symbol_bad = 0,  
            #     access = True     #
            # )
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
    
    
    # дополнительная функция получения словаря статей
def function_show_article_2(dot, key_article, photo_clas, dict_draft):
    if dot:
        key_article = True  
        count = 0 
        list_draft = []
        for i in dot:
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
            
# проверка словаря статей
def function_show_article(clas, photo_clas, filter_list = False):
    key_article = False                                                     # ключ статей
    dict_draft = {}
    print(filter_list)
    if filter_list == False:
        try:
            dot = clas.objects.all()
        except OperationalError as error:
            print(error)
        else:
            key_article, dict_draft = function_show_article_2(dot, key_article, photo_clas, dict_draft)
    else:
        dot = []
        count = 0
        print(filter_list)
        try:
            dot1 = clas.objects.all()
        except OperationalError as error:
            print(error)
        else:
            for i in dot1:
                print(i)
                for elem in filter_list:
                    print(elem)
                    if elem in i.collection and i not in dot:
                        count += 1
                        dot.append(i)   
        if count!= 0: 
            key_article, dict_draft = function_show_article_2(dot, key_article, photo_clas, dict_draft)
    return key_article, dict_draft 

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

# функция получение списка из строки класса личных настроект пользователя
def list_interest_user(param):
    list_interes = ['ОБЩЕЕ']
    string = ''
    for i, elem in enumerate(param[2:]):
        if elem not in "' ],":
            string += elem
        elif elem == "'" and param[2:][i+1] == ',' or elem == "'" and param[2:][i+1] == ']':
            list_interes.append(string)
            string = ''
        elif elem == "]" or elem == "," or elem == "'":
            pass
    return list_interes


