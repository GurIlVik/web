from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from sqlite3 import OperationalError
from django.contrib.auth.models import User
from personalpage.models import PresentationUser

# отображение главной страницы
def main_page(request):
    list_interest = function_list_interes(request)
    # print(list_interest)
    a = Catalogy.objects.all().order_by('name')  # сортировка списка по имени в базе
    b = ProstoList('prosto_list')
    c = Information_block.objects.all()
    e = Amalker.objects.all()
    predmet_collection_list = []   # В этом списке выбранные категории предметов
    g = chek_User_authenticated(request, 'Регистрация/ВХОД', 'ВЫХОД') # предоставление значений согласно логик
    h = chek_User_authenticated(request, "/", "/logout/")  # предоставление путей согласно логик
    j = f'/personalpage/{str(request.user)}'      # получение имени и питу на личную страницу
    
    # list_interest = list_interest_user(list_interest)
    if list_interest:
        key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock, request, filter_list = list_interest) 
    else:
        key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock, request)     
    # print(key_article)
    # print(dict_article)
    
    context = {
        'a': a,
        "form" : b,
        'form2' : CountText1(),
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
        form2 = CountText1(request.POST)
        print(10)
        if form.is_valid(): 
            print(11)
            form = form.cleaned_data
            print(form)
            predmet_collection_list = method_main_page_1(form['pole']) # В этом списке выбранные категории предметов
            context['key_article'], context['info_blok'] = function_show_article(Information_block, PhotoInfoBlock, request, filter_list = predmet_collection_list) 
            return render(request, 'main/index.html', context)
        elif form2.is_valid():
            print(12)
            print('форма 2')
            form2 = form2.cleaned_data
            article = Information_block.objects.get(id = int(form2['count'][2:]))
            # check_count_article = CountArticle.objects.get(article_count = article)
            # print(article)
            print(form2['count'][0])
            function_count_interes(article, request, form2)
            if list_interest:
                key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock, request, filter_list = list_interest) 
            else:
                key_article, dict_article = function_show_article(Information_block, PhotoInfoBlock, request)      
            context['info_blok'] = dict_article
            context['key_article'] = key_article
            return render(request, 'main/index.html', context)
        print(13)
        return render(request, 'main/index.html', context)
    
    return render(request, 'main/index.html', context)
 
# отображение страницы публикации
def publication(request, author, id):
    print(1)
    c = Information_block.objects.filter(id = id)
    k = Information_block.objects.get(id = id)
    j = f'/personalpage/{str(request.user)}'
    form = CommentUser()
    form2 = CommentForComment()
    form3 = CommentForComment2()
    print('start')
    list_int2 = check_predmet_collection(k.collection)
    acess_comm = function_acess_comment(k.access, request, list_int2)
    
    # print(acess_comm) # допуск к комментированию
    photo_autor = PresentationUser.objects.get(user=k.author).photo
    # # print(photo_autor)
    # print(k.pk)
    key_comments, dict_comments = function_show_comments(ArticleСomments, request, k.pk)
    # print(key_comments)
    # print(dict_comments)
    blok_publik = function_show_publik(id)
    count_int_art = count_for_article_publication(CountArticle, request, k)
    # count_int_com = count_for_article_publication(CountComment, request, k)
    # count_int_com2 = count_for_article_publication(CountComment2, request, k)
    context = {'a' : author,
            'info_blok' : c, 
            'blok_publik' : blok_publik,
            'puth_paesonalpage' : j,
            'form' : form,
            'key_comments' : key_comments,
            'dict_comments' : dict_comments,
            'model' : dict_comments,
            'form2' : form2,
            'form3' : form3,
            'photo_autor' : photo_autor,
            'acess_comm' : acess_comm,
            'form4' : CountText1(),
            'form5' : CountText2(),
            'form6' : CountText3(),
            "simbol_4" : count_int_art,
            } 
    if request.method == 'POST':
        form = CommentUser(request.POST)
        form2 = CommentForComment(request.POST)
        form3 = CommentForComment2(request.POST)
        form4 = CountText1(request.POST)
        form5 = CountText2(request.POST)
        form6 = CountText3(request.POST)
        print(form6)
        if form.is_valid(): 
            print('комментарий 2')
            form = form.cleaned_data
            asss = ArticleСomments.objects.create(autor_publication = User.objects.get(username = author),                                        # ID статьи автора статьи
                publication = k,
                autor_message = request.user,                               #  имя комментатора
                text_message = form['comment'],                                        #  текст комментария
                count_symbol_ok = 0,                                        # 
                count_symbol_bad = 0,  
            )
            key_comments, dict_comments = function_show_comments(ArticleСomments, request, k.pk)
            context['key_comments'] = key_comments
            context['dict_comments'] = dict_comments
            return render(request, 'main/publication.html', context)
        
        elif form3.is_valid():
            form3 = form3.cleaned_data
            print('комментарий 3')
            dert = ArticleСommentsTwo.objects.get(id=form3['comment2_id']).comment.pk
            print(dert)
            print(form3)
            asss = ArticleСommentsTwo.objects.create(
                author_comment = form3['author_comment'],
                comment = ArticleСommentsTwo.objects.get(id=form3['comment2_id']).comment,
                author_re_comment = User.objects.get(username = request.user),
                text_message = form3['comment2'],
                count_symbol_ok = 0,                                     
                count_symbol_bad = 0, 
            )
            key_comments, dict_comments = function_show_comments(ArticleСomments, request, k.pk)
            context['key_comments'] = key_comments
            context['dict_comments'] = dict_comments
            return render(request, 'main/publication.html', context)
        elif form2.is_valid(): 
            form2 = form2.cleaned_data
            print('комментарий 2')
            # print(form2)
            asss = ArticleСommentsTwo.objects.create(
                author_comment = str(ArticleСomments.objects.get(id=form2['comment2_id']).autor_message),
                comment = ArticleСomments.objects.get(id=form2['comment2_id']),
                author_re_comment = User.objects.get(username = request.user),
                text_message = form2['comment2'],
                count_symbol_ok = 0,                                     
                count_symbol_bad = 0, 
            )
            key_comments, dict_comments = function_show_comments(ArticleСomments, request, k.pk)
            context['key_comments'] = key_comments
            context['dict_comments'] = dict_comments
            return render(request, 'main/publication.html', context)
        elif form4.is_valid():
            print('счетчик1')
            form4 = form4.cleaned_data
            print(form4)
            article = k
            function_count_interes(article, request, form4)
            count_int_art = count_for_article_publication(CountArticle, request, k)
            context['simbol_4'] = count_int_art
            context['blok_publik'] = function_show_publik(id)
            return render(request, 'main/publication.html', context)
        elif form5.is_valid():
            print('счетчик2')
            form5 = form5.cleaned_data
            print(form5)
            return render(request, 'main/publication.html', context)
        elif form6.is_valid():
            print('счетчик3')
            form6 = form6.cleaned_data
            print(form6)
            return render(request, 'main/publication.html', context)
        else:
            return HttpResponse('ЧТО_ТО ОПЯТЬ НЕ ТАК')
    else:
        print('без запроса')
        return render(request, 'main/publication.html', context)
    
    # дополнительная функция получения словаря статей
def function_show_article_2(dot, key_article, photo_clas, dict_draft, request,):
    user = request.user
    if dot:
        key_article = True  
        count = 0 
        list_draft = []
        simbol_count = False
        list_count_draft = []
        for i in dot:
            # print('функция счетчика после фор')
            # print(i)
            res = photo_clas.objects.filter(location__pk = i.pk) # запрос получения фотограпфий через id
            if res:
                for j in res:
                    list_draft.append(j.image)
                    count += 1
            else:
                list_draft.append(False)
            dict_photo = {count : list_draft}
            # print('мловарь', dict_photo)
            # print('list draft', list_draft)
            simbol_c = ''
            if user.is_authenticated:
                simbol_c = CountArticle.objects.filter(author_count = user, article_count=i.pk)
            else:
                simbol_c = CountArticle.objects.filter(article_count=i.pk)    
            for j in simbol_c:
                simbol_count = j.simbol
            list_count_draft.append(dict_photo)
            list_count_draft.append(simbol_count)
            dict_draft[i] = list_count_draft
            list_draft = []
            count = 0   
            simbol_count = False
            list_count_draft = [] 
    return key_article, dict_draft
            
# проверка словаря статей
def function_show_article(clas, photo_clas, request, filter_list = False):
    key_article = False                                                     # ключ статей
    dict_draft = {}
    # print(filter_list)
    if filter_list == False:
        try:
            dot = clas.objects.all()
        except OperationalError as error:
            print(error)
        else:
            key_article, dict_draft = function_show_article_2(dot, key_article, photo_clas, dict_draft, request,)
    else:
        dot = []
        count = 0
        # print(filter_list)
        try:
            dot1 = clas.objects.all()
        except OperationalError as error:
            print(error)
        else:
            for i in dot1:
                for elem in filter_list:
                    if elem in i.collection and i not in dot:
                        count += 1
                        dot.append(i)   
        if count!= 0: 
            key_article, dict_draft = function_show_article_2(dot, key_article, photo_clas, dict_draft, request,)
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

# функция подготовки словаря для распечатки статьи 
def function_show_publik(param):
    list_photo = []
    k = Information_block.objects.get(id = param)
    try:
        d = PhotoInfoBlock.objects.filter(location__pk=k.pk)
    except:
        print('нет фото')
    else:
        for elem in d:
            list_photo.append(elem.image)
    dict_pablik = {k : list_photo}
    return dict_pablik 

# функция отображения имеющихся комментариев    
def function_show_comments(param, request, key):
    key_article = False                                                     # ключ статей
    list_draft = {}
    dot = ''
    dict_com = {}
    dict_com2 = {}
    try:
        dot = param.objects.filter(publication=key)
    except OperationalError as error:
        print('ошибочка')
    else:
        key_article = True
        print('в функции function_show_comments')
        
        dot2 = ''
        list_draft2 = []
        simbol = ''
        simbol2 = ''
        
        if dot:
            for i in dot:
                try:
                    dot2 = ArticleСommentsTwo.objects.filter(comment=i.pk)
                except OperationalError as error:
                    print('ошибочка')
                else:
                    if dot2:
                        for j in dot2:
                            # print("Это его второй цикл в котором ошибка ")
                            simbol2 = count_for_article_publication(CountComment2, request, j)
                            # list_draft2.append(ArticleСommentsTwo.objects.get(id=j.id))
                            dict_com2[j] = simbol2
                            # print('это символ2', dict_com2 )
                            list_draft2.append(dict_com2)
                            # print(list_draft2)
                            dict_com2 = {}
                    else:
                        list_draft2 = False
                simbol = count_for_article_publication(CountComment, request, i)
                dict_com[simbol] = list_draft2
                list_draft[i] = dict_com
                # print('ЭТО КОНЕЧНЫЙ ВАРИАНТ -', list_draft )
                list_draft2 = []
                dict_com = {}
                dict_com2 = {}    
    return key_article, list_draft

# функция отображения листа коллкционных предметов  
def function_list_interes(request):
    list_interest = []
    try:
        list_interest = PresentationUser.objects.get(user=request.user).interest
    except:
        print('ну нет интереса')
        list_int = Catalogy.objects.all()
        for elem in list_int:
            list_interest.append(elem.name)
    else: 
        list_interest = list_interest_user(list_interest)
    return list_interest

 # функция проверки допуска для комментирования 
def function_acess_comment(key, request, list_int2):
    res = False
    list_interest = function_list_interes(request)
    param = False
    for i in list_interest:
        for j in list_int2:
            if i == j:
                param = True
                break
    if int(key) == 1 and request.user.is_authenticated:
        res = True
    elif int(key) == 2 and param == True:
        res = True
    return res  

# функция перезаписи счетчиков
def function_count_interes(article, request, form2):
    user = request.user
    check_count_articles = ''
    # print(article)
    # print(request)
    # print(form2['count'][0])
    try:
        check_count_articles = CountArticle.objects.filter(author_count = user, article_count=article)
        print(check_count_articles)
    except:
        print('ошибка распознования пользователя')
        save_count_article(article, request, form2)
    else:
        if check_count_articles:
            for check_count_article in check_count_articles:
                if check_count_article.count_simbol:
                    # print(form2['count'][0])
                    if check_count_article.simbol == form2['count'][0] or check_count_article.simbol == ' ':
                        # print('=')
                        if form2['count'][0] == '+':
                            number = int(article.count_symbol_ok) - 1
                            article.count_symbol_ok = number
                            article.save()
                        elif form2['count'][0] == '-':
                            number = int(article.count_symbol_bad) - 1
                            article.count_symbol_bad = number
                            article.save()
                        check_count_article.simbol = ' '
                        check_count_article.count_simbol = False
                    else:
                        # print('1=')
                        if form2['count'][0] == '+': 
                            print('+')
                            number = int(article.count_symbol_ok) + 1
                            article.count_symbol_ok = number
                            number = int(article.count_symbol_bad) - 1  
                            article.count_symbol_bad = number
                            article.save()
                            check_count_article.simbol = '+'
                        else: 
                            # print('-')  
                            number = int(article.count_symbol_ok) - 1
                            article.count_symbol_ok = number
                            number = int(article.count_symbol_bad) + 1  
                            article.count_symbol_bad = number
                            article.save()  
                            check_count_article.simbol = '-'
                        check_count_article.count_simbol = True
                        check_count_article.save()
                        # print(check_count_article.simbol)
                else:
                    if check_count_article.simbol == ' ' or check_count_article.simbol == form2['count'][0]:
                        check_count_article.count_simbol = True    
                        check_count_article.simbol = form2['count'][0]  
                        # print('wofknv', check_count_article.simbol)
                        check_count_article.save()
                        if form2['count'][0] == '+':    
                            number = int(article.count_symbol_ok) + 1
                            article.count_symbol_ok = number   
                        else:  
                            number = int(article.count_symbol_bad) + 1  
                            article.count_symbol_bad = number
                        article.save()  
                check_count_article.save()         
        else:
            save_count_article(article, request, form2)
            
# функция сохранения счетчиков интереса
def count_for_article(article, form2):
    if form2['count'][0] == "+":
        number = int(article.count_symbol_ok) + 1
        article.count_symbol_ok = number
    elif form2['count'][0] == "-":
        number = int(article.count_symbol_bad) + 1
        article.count_symbol_bad = number
    article.save()
    
# функция сохранения счетчиков интереса    
def save_count_article(article, request, form2):
    asss = CountArticle.objects.create(
        author_count = request.user,
        article_count = article,
        count_simbol = True,
        simbol = form2['count'][0],
    )
    print(asss)
    count_for_article(article, form2)
    
# функция получения знака счетчика комментария если есть
def count_for_article_publication(clas, request, articl):
    count_int = False
    count_ints = False
    if request.user.is_authenticated:
        try:
            count_ints = clas.objects.filter(author_count = request.user, article_count=articl)
        except OperationalError as error:
            print(error) 
            print('ytn nfrjq pfgbcb djj,ot')
        else:
            pass
            # print('xnj-nj tcnm ')
            
        if count_ints:
            for i in count_ints:
                count_int = i.simbol 
        else:
            
            count_int = False
    return count_int      

# получение списка коллекций
def check_predmet_collection(param):
    list_int2 = []    # получение списка предметов
    strin = ''
    for elem in param:
        if elem not in ', ':
            strin += elem
        elif elem ==',':
            list_int2.append(strin)
            strin = ''
    return list_int2


