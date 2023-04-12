from django.db import models

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

