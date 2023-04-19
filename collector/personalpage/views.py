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
    nik_reguest = getting_nickname_request(request)  # получение имени пришедшего пользователя
    search_user = user_page_search(user)  # получение булевого есть ли такой пользователь (тру/фальш)
    registered_user = chek_user_register(request)  # логик тру пользователь зарегистрирован или нет фальш
    # print(user)             # имя страницы пользователя
    # print(nik_reguest)      # имя зашедшего на страницу
    # print(search_user)      # тру-страница есть фальш - страницы нет
    # print(registered_user)  # тру-зарегистрирован | нет фальш
    a = Information_block.objects.all()
    b = user
    c = NewArticleForm()
    password = chek_user_access(user, nik_reguest) # логик - тру страница индивида или нет фальш
    d = NewArticle.objects.filter(author=user)
    e = PersonalInformationUser()
    f = Catalogy.objects.all().order_by('name')
    g = ''                                      # логика получения информации о заполненности анкеты потльзователя
    h = None                                    # отображение информации о пользователи из модели
    k = []                                       #   отображение коллекционного листа
    l = AllowanceForm()
    m = SpecialInfoUser()
    title = 'Кабинет'
    menu = ['К СЕБЕ', 'НА ГЛАВНУЮ', 'РЕГИСТРАЦИЯ',]
    menu1 = ['НАСТРОЙКИ', 'НАПИСАТЬ', 'К ОБЩЕСТВУ', 'ВЫХОД',]
    menu2 = ['К СЕБЕ', 'К ОБЩЕСТВУ', 'ВЫХОД',]
    
    if password:                                           # если это страница юзера
        menu = menu1
        g = PresentationUser.objects.filter(user__username = nik_reguest)
        for i in g:
            h = i
            k = func_str_for_list(i.interest)
            print(k)
            if i.in_publishid == True:
                g = True
            else:
                g = False
    elif registered_user:
        menu = menu2
    print(d)
    for i in d:
        print(i.author)
    print(k)
    context = {'nik_name' : nik_reguest,
                   'access' : password,
                   'register' : registered_user,
                   'information_block' : a,
                   'nik_user' : b, 
                   'form' : c,
                   'for_editorial_office' : d,
                   'title' : title,
                   'menu' : menu,
                   'form_info' : e,
                   'list_a': f,
                   'logik_1': g,
                   'persona' : h,
                   'predmets' : k,
                   'acess_form' : l,
                   'secret_form' : m,
                   }
    if search_user == False:
        return HttpResponse('такого пользователя нет')
    else:
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
                        # time_publication = models.DateTimeField(auto_now_add=True)
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
                print(form_user2['for_page'])
                print(form_user2['for_inform'])
                print(form_user2['for_messeng'])
                l = Allowance(
                    user = request.user,
                    for_page = function_acess(form_user2['for_page']),
                    for_inform = function_acess(form_user2['for_inform']),
                    for_messeng = function_acess(form_user2['for_messeng']),
                    in_publishid = True,
                )
                l.save()
                print(l.for_page)
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
                print(m.name)
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
            
            
def function_acess(info):
    res = 0
    print(len(str(info)))
    if 20 < len(str(info)) < 33:
        res = 1
    if len(str(info)) > 33:
        res = 2
    print(res)
    return res