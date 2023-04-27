from django.db import models
from django.contrib.auth.models import User

# модель рекламного блока
class Amalker(models.Model):
    name_seller = models.CharField(max_length=250)
    tabloid = models.TextField(blank=True)
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)
    time_ending = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=250) # указывается предмет или список ...ов коллекции
    class Meta:
        verbose_name_plural = 'Реклама' 
        

# модель категории статьи
class Category(models.Model):
    name = models.TextField(blank=False, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Список(Статья.Объявление.Философия)'
 
# модель представления списка объявлений
class Advertisement(models.Model):
    name = models.CharField(max_length=50, blank=False,)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Список(Услуги,ищу,продаю)'
 
# Основная модель отображения списка предметов коллекционирования 
class Catalogy(models.Model):
    name = models.CharField(max_length=50, blank=False,)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Предмет коллекционирования(В1)'

# допуск к комментированию статей    
class AllowanceComment(models.Model):
    name = models.CharField(max_length=50, blank=False,)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Список(никому,одноклубникам,соколлекционерам)'

   
# вспомогательная модель поиска по интерессу 
class TopicInterest(models.Model):
    name = models.CharField(max_length=250, null=True)
    

# модель размещения блока информации
class Information_block(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    categories = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'категория')
    topic = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'предмет')
    title = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'название')
    text = models.TextField(null=True, blank=True, verbose_name = 'текст') 
    in_publishid = models.BooleanField(default=False)         # Если  инфо опубликованна
    time_publication = models.DateTimeField(auto_now_add=True, auto_now = False,)
    count_symbol_ok = models.CharField(max_length=5)
    count_symbol_bad = models.CharField(max_length=5)
    access = models.CharField(max_length=5)
    
    class Meta:
        verbose_name_plural = 'Статьи'
        
# ФОТОграфии для публикации
class PhotoInfoBlock(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',)
    location = models.ForeignKey(Information_block, related_name='photo', on_delete=models.CASCADE)

# модель представления комментария 
class ArticleСomments(models.Model):  
#     whom_message = models.CharField(max_length=50)
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)
#     whose_message = models.CharField(max_length=50)
#     text_message = models.TextField(blank=True)
#     count_symbol_ok = models.CharField(max_length=5)
#     symbol_bad = models.CharField(max_length=1, null=False)               
#     count_symbol_bad = models.CharField(max_length=5, null=True)
#     comment_article = models.CharField(max_length=50, null=False)
#     write_author = models.CharField(max_length=50, null=False)
#     access = models.BooleanField(null=False)
    class Meta:
        verbose_name_plural = 'комментарий'

# модель представления комментария на комментарий
class ArticleСommentsTwo(models.Model):  
#     whom_message = models.CharField(max_length=50)                              # кому ответ
    time_publication = models.TimeField(auto_now_add=True, auto_now = False,)   
#     whose_message = models.CharField(max_length=50)                             # кто ответил
#     text_message = models.TextField(blank=True)
#     count_symbol_ok = models.CharField(max_length=5)                            # счетчик +
#     id_articl = models.CharField(max_length=1, null=False)                      # id статьи
#     count_symbol_bad = models.CharField(max_length=5, null=True)                # счетчик -
#     id_comment = models.CharField(max_length=50, null=False)                    # id коммента
#     write_author = models.CharField(max_length=50, null=False)
#     access = models.BooleanField(null=False)
    class Meta:
        verbose_name_plural = 'комм на комм'