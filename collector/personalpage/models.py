from django.db import models

# Модель записи сообщения на сохранение под дальнейшую редакцию
class NewArticle(models.Model):
    author = models.CharField( max_length=100, null=True, blank=True)
    categories = models.CharField( max_length=100, null=True, blank=True)
    topic = models.CharField( max_length=100, null=True, blank=True)
    title = models.CharField( max_length=100, null=True, blank=True)
    text = models.TextField(null=True, blank=True) 
    photo = models.FileField(null=True, blank=True)

