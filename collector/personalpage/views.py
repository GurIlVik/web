from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
# from django.contrib.auth import authenticate, login, logout
from .forms import *
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import urls
from main.models import Information_block, Catalogy
from .models import NewArticle, PresentationUser, Allowance, Photo
from main.views import method_main_page_1
from django.core.files.base import ContentFile


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
    list_collection_guest, key_guest, info_guest = func_list_colliction(request, nik_reguest)       # лист предметов коллекции пришедшего    
    list_collection_owner, key_owner, info_owner = func_list_colliction(request, user)              # лист предметов коллекции хозяина
    groupmates = func_list_check(list_collection_guest, list_collection_owner) # проверка есть ли в списке похожие интересы есть - правда нет -ложь
                                                    
    acesses = Allowance.objects.filter(user__username = user)                # получение допусков из базы
    if acesses:
        acess_key, acess_page, acess_info, acess_mass = function_acess_user(user)
    if password == False:
        if (acess_page == 3) or (registered_user == False and acess_page == 1) or (groupmates == False and acess_page == 2):
            return redirect(f'/personalpage/{user}/block_page')             # перенаправление гостя на страницу блокировки
        else:
            return redirect(f'/personalpage/{user}/reception')              # перенаправление гостя в приемную   
        
    key_article, dict_draft = function_show_drafts(user)    # получение ключа и словаря для отображения страницы
    
    a = Information_block.objects.all()
    b = user
    c = NewArticleForm()
    e = PersonalInformationUser()
    f = Catalogy.objects.all().order_by('name')
    m = SpecialInfoUser()
    title = 'Кабинет'
   
    menu1 = ['НАСТРОЙКИ', 'НАПИСАТЬ', 'К ОБЩЕСТВУ', 'ВЫХОД',]
    
 

    context = {'nik_name' : nik_reguest,
                   'register' : registered_user,
                   'information_block' : a,
                   'nik_user' : b, 
                   'form' : c,
                   'for_editorial_office' : dict_draft,
                   'title' : title,
                   'menu' : menu1,
                   'form_info' : e,
                   'list_a': f,
                   'logik_1': key_owner,     # отображение в случае если 1ая форма заполнена(1) не заполнена(0)
                   'logik_2': function_show_specinf(user),  # отражение в случае если есть спец инфоормация
                   'persona' : info_owner,   # отображение информации о пользователе
                   'predmets' : list_collection_owner, # отображение коллекционного листа
                   'acess_form' : AllowanceForm(),  # форма для забора допусков от пользователя
                   'secret_form' : m,
                #    'acess_key' : acess_key,
                   'acess_page' : acess_page,
                   'acess_info' : acess_info,
                   'acess_mass' : acess_mass,                                               # ключ черновиков
                   'key_article' : key_article, 
                   }
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        
        form_user1 = PersonalInformationUser(request.POST, request.FILES)
        form_user2 = AllowanceForm(request.POST)
        form_user3 = SpecialInfoUser(request.POST)
        print(1)
        if form.is_valid():
            print(2)
            cd = form.cleaned_data
            if 'memory' in request.POST:
                print(21)
                function_write_draft(request, cd)
            elif 'write' in request.POST:
                print(22)
                function_write_clean_copy(request, cd, b)
            elif 'delete' in request.POST:
                print(23)
                pass
            else: 
                print(3)
                for key, elem in request.POST.items():
                    print(4)
                    if 'memor_' in key:
                        print(4.5)
                        function_rewrite_draft(cd, request, int(key[6:]))
                    elif 'writ_' in key:
                        function_delete_draft(int(key[5:]))
                        function_write_clean_copy(cd, b)
                    elif 'delet_' in key:
                        function_delete_draft(int(key[6:]))
                    else:
                        ('что-то идет не так')
                
                                                             
                    print(key)
                print(request.POST)
                print('вот так хрень нельзя же цифру')
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

# получение доступа по странице
def function_acess_for_page(ace, reg, group):
    res = False
    if (ace == 0) or (ace == 1 and reg == True) or (ace == 2 and group == True):
        res = True
    return res
    

# ОТОБРАЖЕНИЕ страницы в приемной
def personal_page_reception(request, user):
    nik_reguest = getting_nickname_request(request)                         # получение имени пришедшего пользователm
    acess_info = 3                                                           # доступ к информации
    acess_mass = 3 
    acesses = Allowance.objects.filter(user__username = user)                # получение допусков из базы
    registered_user = chek_user_register(request)                            # логик тру вошедший зарегистрирован Ё нет - фальш
    list_collection_guest, key_guest, info_guest = func_list_colliction(request, nik_reguest)       # лист предметов коллекции пришедшего    
    list_collection_owner, key_owner, info_owner = func_list_colliction(request, user)              # лист предметов коллекции хозяина
    groupmates = func_list_check(list_collection_guest, list_collection_owner) # проверка есть ли в списке похожие интересы есть - правда нет -ложь
    
    acesses = Allowance.objects.filter(user__username = user)                # получение допусков из базы
    if acesses:
        acess_key, acess_page, acess_info, acess_mass = function_acess_user(user)
        
    acesses_guest_info = function_acess_for_page(acess_info, registered_user, groupmates) # допуск к информации если правда
    acesses_guest_mess = function_acess_for_page(acess_mass, registered_user, groupmates) # допуск к мессенжеру если правда
    context = {
        'title' : 'Приемная',
    }
    return render(request, 'personalpage/reception.html', context)


    
    
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
    key_info = None
    person_info = None
    list_coll = PresentationUser.objects.filter(user__username = us)
    if list_coll:                                                        # логика получения листа колекций гостя из базы
        list_coll = PresentationUser.objects.get(user__username = us)
        list_collection_guest = func_str_for_list(list_coll.interest)
        key_info = list_coll.in_publishid
        person_info = list_coll
    return list_collection_guest, key_info, person_info

# Функция получения ключа на отражение окна спец информации
def function_show_specinf(user):
    res = False
    param = InfoUser.objects.filter(user__username = user)
    if param:
        param = InfoUser.objects.get(user__username = user)
        res = param.in_publishid
    return res

# функция поиска совпадений по спискам коллекций
def func_list_check(l1, l2):
    for i in l1:
        if i != 'ОБЩЕЕ':
            if i in l2:
                return True
    return False

# функция получения ключа и словаря для отображения черновиков на странице
def function_show_drafts(user):
    key_article = False                                                     # ключ статей
    d = NewArticle.objects.filter(author__username = user)
    dict_draft = {}
    if d:
        key_article = True   
        list_draft = []
        for i in d:
            res = Photo.objects.filter(location__pk = i.pk) # запрос получения фотограпфий через id
            if res:
                for j in res:
                    list_draft.append(j.image)
            else:
                list_draft.append(False)
            dict_draft[i] = list_draft
            list_draft = []
    return key_article, dict_draft 

# функция записи из формы в модель черновика - статьи с фотографиями
def function_write_draft(request, cd):
    location = NewArticle.objects.create(author=request.user, 
                                        title=cd['title'], 
                                        text=cd['text'], 
                                        categories=cd['categories'], 
                                        topic = cd['topic'])
    for f in request.FILES.getlist('photo'):
        data = f.read()
        # photo = Photo.location.set(location)  # отображает в админке но не показывает в другом
        photo = Photo(location=location)   # работало с ключем ForeignKey
        photo.image.save(f.name, ContentFile(data))
        photo.save()

# функция записи из формы в модель чистовика - статьи с фотографиями       
def function_write_clean_copy(cd, b):
    с = Information_block.objects.create(
        picture_author = 'фото',
        page_author = b,       # ник автора с отправкой на его страницу
        categories = cd['categories'],        # категории по списку предметов коллекционирования
        topic_interest = cd['topic'],      # категории по списку интереса и поиска
        table_contents = cd['title'],
        text_contents = cd['text'],
        symbol_ok = 'ok',
        count_symbol_ok = 0,
        symbol_bad = 'out',
        count_symbol_bad = 0,
        comment_article = 'пока вопрос',     # комментарии который необходимо сделать сноской и следовательно не факт что необходи вообще
        write_author = 'писать автору', 
        access = True)

# функция удаления черновика
def function_delete_draft(key):
    memory_elem = NewArticle.objects.get(id = key)
    memory_elem.delete()

# функция перезаписи черновика    
def function_rewrite_draft(cd, request, key):
    print(cd['title'])
    
    print(type(cd['topic']))
    memory_elem = NewArticle.objects.get(id = key)
    
    print(memory_elem.title)
    
    memory_elem.title=cd['title'], 
    
   
    memory_elem.text=cd['text'], 
    memory_elem.categories=cd['categories'], 
    memory_elem.topic = str(cd['topic'])
    memory_elem.save()
    
    for fail_f in request.FILES.getlist('photo'):
        
        data = fail_f.read()
        photo = Photo(location=memory_elem)   # работало с ключем ForeignKey
        photo.image.save(fail_f.name, ContentFile(data))
        photo.save()
        
        