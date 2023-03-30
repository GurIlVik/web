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
   
# вспомогательная модель поиска по интерессу 
class TopicInterest(models.Model):
    name = models.CharField(max_length=250, null=True)

# модель размещения блока информации
class Information_block(models.Model):
    picture_author = models.CharField(max_length=250)
    page_author = models.CharField(max_length=250)          # ник автора с отправкой на его страницу
    time_publication = models.DateTimeField(auto_now_add=True)
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
    time_publication = models.DateTimeField(auto_now_add=True)
    whose_message = models.CharField(max_length=50)
    text_message = models.TextField(blank=True)
    count_symbol_ok = models.CharField(max_length=5)
    symbol_bad = models.CharField(max_length=1)
    count_symbol_bad = models.CharField(max_length=5)
    comment_article = models.CharField(max_length=50)
    write_author = models.CharField(max_length=50)
    access = models.BooleanField(null=True)
    
