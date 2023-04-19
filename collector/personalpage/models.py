from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# Модель записи сообщения на сохранение под дальнейшую редакцию
class NewArticle(models.Model):
    author = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'автор')
    categories = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'категория')
    topic = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'предмет')
    title = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'название')
    text = models.TextField(null=True, blank=True, verbose_name = 'текст') 
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'фото')
    
    class Meta:
        verbose_name = 'Статья'                 # отображение в админе единственное число
        verbose_name_plural = 'Статьи'          # отображение в админе мн число
        ordering = ['categories', '-topic']      # отображение в админе сортировка - минус обратная сортировка
        # для отображения в админке страницы на русском необходимо перейти в аррс.пи 

# МОДЕЛЬ разделения на продавцов и коллекционеров 
class Professional(models.Model):
    name = models.CharField( max_length=50, db_index=True, verbose_name = 'профессия')
    class Meta:
         verbose_name_plural = 'Род деятельности'                 # отображение в админе единственное число      
    def __str__(self):
        return self.name

# МОДЕЛЬ ФОРМЫ по ДОПУСКу К на личную страницу
class AllowanceModel1(models.Model):
    name = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'Вид допуска на страницу')  # 0 ни кому, 1 регистрированным, 2 всем
    class Meta: 
        verbose_name_plural = 'Вид допуска на личную страницу'                   # отображение в админе единственное число      
    def __str__(self):
        return self.name  
    
# МОДЕЛЬ ФОРМЫ по ДОПУСКу К личной информации
class AllowanceModel2(models.Model):
    name = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'Вид допуска на страницу')  # 0 ни кому, 1 регистрированным, 2 всем
    class Meta: 
        verbose_name_plural = 'Вид допуска к личной информации'                   # отображение в админе единственное число      
    def __str__(self):
        return self.name   
    
# МОДЕЛЬ ФОРМЫ по ДОПУСКу К мессенжеру
class AllowanceModel3(models.Model):
    name = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'Вид допуска на страницу')  # 0 ни кому, 1 регистрированным, 2 всем
    class Meta: 
        verbose_name_plural = 'Вид допуска к мессенжеру'                   # отображение в админе единственное число      
    def __str__(self):
        return self.name  
    
# ПРОМЕЖУТОЧНАЯ ДЛЯ ФОРМЫ    
class AllowanceModel(models.Model): 
    for_page = models.ForeignKey(AllowanceModel1, on_delete=models.CASCADE)  # 0 ни кому, 1 регистрированным, 2 всем
    for_inform = models.ForeignKey(AllowanceModel2, on_delete=models.CASCADE)  # 0 ни кому, 1 регистрированным, 2 всем
    for_messeng = models.ForeignKey(AllowanceModel3, on_delete=models.CASCADE)

    
# МОДЕЛЬ ДОПУСКОВ НА ЛИЧНУЮ СТРАНИЦУ И К ИНФОРМАЦИИ CФОРМИРОВАННЫЙ ПО БУЛЕАН
class Allowance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    for_page = models.BooleanField(default=False)  # 0 ни кому, 1 регистрированным, 2 всем
    for_inform = models.BooleanField(default=False)  # 0 ни кому, 1 регистрированным, 2 всем
    for_messeng = models.BooleanField(default=False)  # 0 ни кому, 1 регистрированным, 2 всем
    class Meta:
        verbose_name_plural = 'ДОПУСК ЮЗЕРОВ'                   # отображение в админе единственное число      
    def __str__(self):
        return self.user    

# МОДЕЛЬ ОТОБРАЖЕНИЕ ЛИЧНОЙ ИНФОРМАЦИИ 
class PresentationUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # nikname = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'НИК')
    photo = models.ImageField(upload_to=f"photos/%Y/%m/%d/", verbose_name='Фото')
    # photo = models.ImageField(upload_to=f"photos/{User.username}/%Y/%m/%d/", verbose_name='Фото')
    profession = models.ForeignKey('Professional', on_delete=models.PROTECT, verbose_name='Род деятельности')        # коллекционер/продавец
    FFP = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'ФФП')
    interest = models.CharField( max_length=255, null=True)  # список инетересующих тем
    in_publishid = models.BooleanField(default=False)         # Если  инфо опубликованна
    class Meta:
        verbose_name = 'ВИЗИТКА'
        verbose_name_plural = 'ВИЗИТКА'      
    def __str__(self):
        return str(self.user)
    
 # МОДЕЛЬ ОТОБРАЖЕНИЕ СЕКРЕТНОЙ  ИНФОРМАЦИИ  ПОЛЬЗОВАТЕЛЯ 
class InfoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'ИМЯ')
    name_last = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'Отчество')
    name_first = models.CharField( max_length=100, null=True, blank=True, verbose_name = 'Фамилия')
    telephon = models.IntegerField( null=True, verbose_name = 'телефон')
    def __str__(self):
        return self.user
    class Meta:
        verbose_name_plural = 'Секретная' 