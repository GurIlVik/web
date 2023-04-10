from django.db import models

# модель рекламного блока
class Amalker(models.Model):
    name_seller = models.CharField(max_length=250)
    tabloid = models.TextField(blank=True)
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)
    time_ending = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=250) # указывается предмет или список ...ов коллекции

# основная модель предмета коллекционирования   
class Category(models.Model):
    name = models.TextField(blank=False, unique=True)
    
    def __str__(self):
        return self.name
    
# Допуск к статье предмета коллекционирования ВРЕМЕННО ПУСТАЯ МОДЕЛЬ
class Allowance(models.Model):            
    allowance_commit = models.BooleanField(null=True)   # допуск к комментам
   
# вспомогательная модель поиска по интерессу 
class TopicInterest(models.Model):
    name = models.CharField(max_length=250, null=True)

# модель размещения блока информации
class Information_block(models.Model):
    picture_author = models.CharField(max_length=250)
    page_author = models.CharField(max_length=250)          # ник автора с отправкой на его страницу
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)
    categories = models.CharField(max_length=250)           # категории по списку предметов коллекционирования
    topic_interest = models.CharField(max_length=250)       # категории по списку интереса и поиска
    table_contents = models.CharField(max_length=250)
    text_contents = models.TextField(blank=True)
    symbol_ok = models.CharField(max_length=1)
    count_symbol_ok = models.CharField(max_length=5)
    symbol_bad = models.CharField(max_length=1)
    count_symbol_bad = models.CharField(max_length=5)
    comment_article = models.CharField(max_length=50)       # комментарии который необходимо сделать сноской и следовательно не факт что необходи вообще
    write_author = models.CharField(max_length=50)
    access = models.BooleanField(null=True)

# модель представления комментария 
class Article_comments(models.Model):  
    whom_message = models.CharField(max_length=50)
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)
    whose_message = models.CharField(max_length=50)
    text_message = models.TextField(blank=True)
    count_symbol_ok = models.CharField(max_length=5)
    symbol_bad = models.CharField(max_length=1, null=False)               
    count_symbol_bad = models.CharField(max_length=5, null=True)
    comment_article = models.CharField(max_length=50, null=False)
    write_author = models.CharField(max_length=50, null=False)
    access = models.BooleanField(null=False)
    

# модель представления комментария на комментарий
class Article_commentsTwo(models.Model):  
    whom_message = models.CharField(max_length=50)                              # кому ответ
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)   
    whose_message = models.CharField(max_length=50)                             # кто ответил
    text_message = models.TextField(blank=True)
    count_symbol_ok = models.CharField(max_length=5)                            # счетчик +
    id_articl = models.CharField(max_length=1, null=False)                      # id статьи
    count_symbol_bad = models.CharField(max_length=5, null=True)                # счетчик -
    id_comment = models.CharField(max_length=50, null=False)                    # id коммента
    write_author = models.CharField(max_length=50, null=False)
    access = models.BooleanField(null=False)

