from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# from django.contrib.auth import authenticate, login, logout
from .forms import *
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import urls
from main.models import Information_block, Catalogy
from .models import NewArticle, PresentationUser, Allowance
from main.views import method_main_page_1



# @ login_required
def personal_page(request, user): 
    if user_page_search(user) == False:
        return redirect(f'/personalpage/{user}/mistake')                    #  отправка на страницу ошибка если пользвоателя нет
    nik_reguest = getting_nickname_request(request)                         # получение имени пришедшего пользователm
    password = chek_user_access(user, nik_reguest)                          # правда - если пришедший хозяин страницы
    # значения допусков по умолчанию 3 - никому 2 одногрупникам 1 членам 0 всем
    acess_key = False                                                        # есть ли доступ
    acess_page = 3                                                           # доступ на страницу
    acess_info = 3                                                           # доступ к информации
    acess_mass = 3                                                           # доступ к мессенжеру
    
    registered_user = chek_user_register(request)                            # логик тру вошедший зарегистрирован Ё нет - фальш
    list_collection_guest = func_list_colliction(request, nik_reguest)       # лист предметов коллекции пришедшего    
    list_collection_owner = func_list_colliction(request, user)              # лист предметов коллекции хозяина
    groupmates = func_list_check(list_collection_guest, list_collection_owner) # проверка есть ли в списке похожие интересы есть - правда нет -ложь
    
    if password == True:                                                     # получение допусков из базы
        acesses = Allowance.objects.filter(user__username = user)
        if acesses:
            acess_key, acess_page, acess_info, acess_mass = function_acess_user(user)
    if password == False:
        if acess_page == 3 or registered_user == False and acess_page == 1 or groupmates == False and acess_page == 2:
            return redirect(f'/personalpage/{user}/block_page')             # перенаправление гостя на страницу блокировки
        else:
            return redirect(f'/personalpage/{user}/reception')              # перенаправление гостя в приемную   

    
    
    a = Information_block.objects.all()
    b = user
    c = NewArticleForm()
    password = chek_user_access(user, nik_reguest) # логик - тру страница индивида или нет фальш
    d = NewArticle.objects.filter(author=user)
    e = PersonalInformationUser()
    f = Catalogy.objects.all().order_by('name')
    g = False                                     # логика получения информации о заполненности анкеты потльзователя форма1
    h = None                                    # отображение информации о пользователи из модели
    k = []                                       #   отображение коллекционного листа
    l = AllowanceForm()
    m = SpecialInfoUser()
    title = 'Кабинет'
    menu = ['К СЕБЕ', 'НА ГЛАВНУЮ', 'РЕГИСТРАЦИЯ',]
    menu1 = ['НАСТРОЙКИ', 'НАПИСАТЬ', 'К ОБЩЕСТВУ', 'ВЫХОД',]
    menu2 = ['К СЕБЕ', 'К ОБЩЕСТВУ', 'ВЫХОД',]

  
    context = {'nik_name' : nik_reguest,
                   'access' : password,
                   'register' : registered_user,
                   'information_block' : a,
                   'nik_user' : b, 
                   'form' : c,
                   'for_editorial_office' : d,
                   'title' : title,
                   'menu' : menu1,
                   'form_info' : e,
                   'list_a': f,
                   'logik_1': g,     # отображение в случае если 1ая форма заполнена(1) не заполнена(0)
                   'persona' : h,
                   'predmets' : k,
                   'acess_form' : l,
                   'secret_form' : m,
                   'acess_key' : acess_key,
                   'acess_page' : acess_page,
                   'acess_info' : acess_info,
                   'acess_mass' : acess_mass,
                   }
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        form_user1 = PersonalInformationUser(request.POST, request.FILES)
        form_user2 = AllowanceForm(request.POST)
        form_user3 = SpecialInfoUser(request.POST)
        print(1)
        if form.is_valid():
            cd = form.cleaned_data
            if 'memory' in request.POST:
                cd = NewArticle.objects.create(author=b, title=cd['title'], 
                                                text=cd['text'], photo=cd['photo'], 
                                                categories=cd['categories'], topic = cd['topic'])
                return render(request, 'personalpage/index.html', context)
            elif 'write' in request.POST:
                с = Information_block.objects.create(
                    picture_author = 'фото',
                    page_author = b,       # ник автора с отправкой на его страницу
                    categories = c['categories'],        # категории по списку предметов коллекционирования
                    topic_interest = c['topic'],      # категории по списку интереса и поиска
                    table_contents = c['title'],
                    text_contents = c['text'],
                    symbol_ok = 'ok',
                    count_symbol_ok = 0,
                    symbol_bad = 'out',
                    count_symbol_bad = 0,
                    comment_article = 'пока вопрос',     # комментарии который необходимо сделать сноской и следовательно не факт что необходи вообще
                    write_author = 'писать автору', 
                    access = True)
                return render(request, 'personalpage/index.html', context)
            elif 'delete' in request.POST:
                return render(request, 'personalpage/index.html', context)
        elif form_user1.is_valid():
            form_user1 = form_user1.cleaned_data
            f = PresentationUser(
            user = request.user,
            # nikname = request.user,
            photo = form_user1['photo'],
            profession = form_user1['profession'],       # коллекционер/продавец
            interest = method_main_page_1(form_user1['interest']),  # список инетересующих тем
            in_publishid = True,)
            f.save()
            return render(request, 'personalpage/index.html', context)
        elif form_user2.is_valid():
            form_user2 = form_user2.cleaned_data
            l = Allowance(
                user = request.user,
                for_page = function_acess(form_user2['for_page']),
                for_inform = function_acess(form_user2['for_inform']),
                for_messeng = function_acess(form_user2['for_messeng']),
                in_publishid = True,
            )
            l.save()
            return render(request, 'personalpage/index.html', context)
        elif form_user3.is_valid():
            form_user3 = form_user3.cleaned_data
            m = InfoUser(
                user = request.user,
                name = form_user3['name'],
                name_last = form_user3['name_last'],
                name_first = form_user3['name_first'],
                telephon = form_user3['telephon'],
                in_publishid = True,
            )
            m.save()
            return render(request, 'personalpage/index.html', context)
        else:
            print('что то идет не так')
            print(form.errors)
            print(form_user1.errors)
            print(form_user2.errors)
            return render(request, 'personalpage/index.html', context)
    return render(request, 'personalpage/index.html', context)


# Функция получения имени пользователя из запроса 
def getting_nickname_request(request):
    as_us = str(User.objects.filter(username=request.user))
    as_us = as_us[18:]
    return as_us[:-3]

# функция проверки наличия страницы пользователя
def user_page_search(user):
    for us in User.objects.all():
        if user == us.username:
            return True
    return False

# функция получения логики (страница ли пользователя)
def chek_user_access(user, nik_reguest):
    if user == nik_reguest:
        return True
    return False

# логика зарегистрированость пользователя
def chek_user_register(request):
    if request.user.is_authenticated:
        return True
    return False
 
# функция преобразования строки из бызы данных в список   
def func_str_for_list(inlist):
    res = []
    string = ''
    for i, elem in enumerate(inlist):
        if i >= 2 and i != len(inlist)-1:
            if elem not in ["'", " ", ","]:
                string += elem
            elif elem == "'" and string != '':
                res.append(string)
                string = ''
    return res
            
# функция получения цифрового значения доступов            
def function_acess(info):
    res = 3
    if 10 < len(str(info)) < 19:
        res = 0
    if 20 < len(str(info)) < 33:
        res = 1
    if len(str(info)) > 33:
        res = 2
    return res

# функция получения доступа от хозяина страницы
def function_acess_user(user):
    acesses = Allowance.objects.filter(user__username = user)
    if acesses:
        acesses = Allowance.objects.get(user__username = user)
        n = acesses.in_publishid
        o = acesses.for_page
        p = acesses.for_inform
        q = acesses.for_messeng
    return n, o, p, q

# вспомогательная получение информации из формы хозяина
def function_info_user(list_collection):
    for i in list_collection:
        h = i
        k = func_str_for_list(i.interest)
        if i.in_publishid == True:
            g = True
    return h, k, g





def personal_page_reception(request, user):
    return HttpResponse(f'Это приемная пользователя {user}')

# Функция определения допуска на личную страницу 
def function_permission(request, user):
    ...
    
    
# отражение в случае ошибки 
def personal_page_mistake(request, user):
    context = {'nik_name' : f'Пользователя с псевдонимом {user} не существует.',
               'title' : 'пользователя нет',
                   }
    return render(request, 'personalpage/mistake.html', context)

# отражение в случае блокировки страницы 
def personal_block_page(request, user):
    context = {'nik_name' : f'Приемная {user} закрыта.',
               'title' : 'блок страницы',
                   }
    return render(request, 'personalpage/mistake.html', context)


# вспомогательная функция получения коллекционного листа из БД
def func_list_colliction(request, us):
    list_collection_guest = []
    list_coll = PresentationUser.objects.filter(user__username = us)
    if list_coll:                                                        # логика получения листа колекций гостя из базы
        list_coll = PresentationUser.objects.get(user__username = us)
        list_collection_guest = func_str_for_list(list_coll.interest)
    return list_collection_guest

# функция поиска совпадений по спискам коллекций
def func_list_check(l1, l2):
    for i in l1:
        if i != 'ОБЩЕЕ':
            if i in l2:
                return True
    return False