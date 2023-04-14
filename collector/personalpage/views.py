from django.http import HttpResponse
from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
from .forms import PersonalInformationUser, NewArticleForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import urls
from main.models import Information_block
from .models import NewArticle

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
    title = 'Кабинет'
    menu = ['К СЕБЕ', 'НА ГЛАВНУЮ', 'РЕГИСТРАЦИЯ',]
    menu1 = ['НАСТРОЙКИ', 'НАПИСАТЬ', 'К ОБЩЕСТВУ', 'ВЫХОД',]
    menu2 = ['К СЕБЕ', 'К ОБЩЕСТВУ', 'ВЫХОД',]
    # menu3 = ['К СЕБЕ', 'НА ГЛАВНУЮ', 'РЕГИСТРАЦИЯ',]
    if password:
        menu = menu1
    elif registered_user:
        menu = menu2
    print(d)
    for i in d:
        print(i.author)
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
                   }
    if search_user == False:
        return HttpResponse('такого пользователя нет')
    else:
        if request.method == 'POST':
            form = NewArticleForm(request.POST)
            # form1 = Draft(request.POST)
            
            print(1)
            # print(form)
            if form.is_valid():
                cd = form.cleaned_data
                if 'memory' in request.POST:
                    print(3)
                    cd = NewArticle.objects.create(author=b, title=cd['title'], 
                                                  text=cd['text'], photo=cd['photo'], 
                                                  categories=cd['categories'], topic = cd['topic'])
                    print('memory')
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
                        count_symbol_ok = '12',
                        symbol_bad = 'out',
                        count_symbol_bad = '3',
                        comment_article = 'пока вопрос',     # комментарии который необходимо сделать сноской и следовательно не факт что необходи вообще
                        write_author = 'писать автору', 
                        access = True)
                    print('write')
                    return render(request, 'personalpage/index.html', context)
                elif 'delete' in request.POST:
                    return render(request, 'personalpage/index.html', context)
            # if form1.is_valid():
            #     print('lwrifjbgritugh')
                
                
                # Сюда дописывать функцию сохранения черновика
                
                
            else:
                print('что то идет не так')
                print(form.errors)
            return render(request, 'personalpage/index.html', context)
        return render(request, 'personalpage/index.html', context)
    # if search_user:
    #     password = chek_user_access(user, nik_reguest) # логик - тру страница индивида или нет фальш
    #     context = {'nik_name' : nik_reguest,
    #                'access' : password,
    #                'register' : registered_user,
    #                'information_block' : a,
    #                'nik_user' : b, 
    #                'form_art' : c,
    #                }
    #     return render(request, 'personalpage/index.html', context)
    
    # return HttpResponse('такого пользователя нет')


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
    