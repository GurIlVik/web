# from django.core.exceptions import ValidationError 
# from django.forms.fields import EmailField 
# from django.forms.forms import Form 
from django.db import models
# from django import forms
import secrets

class UserTemporaryModels(models.Model):   
    username = models.EmailField() 
    username2 = models.CharField(max_length = 100, blank=False) 
    password = models.CharField(max_length = 100, blank=False)
    password2 = models.CharField(max_length = 100, blank=False)
    # time_sesion = models.DateTimeField(auto_now_add = True,)
    # key_token = secrets.token_urlsafe()
    # time_token = None
    
    def __str__(self):
        return f'{self.username2}      {self.username}'
    

# все = class.object.all() - получить данные из модели список всех частей из модели
# class.object.filter(username='строке') - получение конкретного значение из модели
# class.object.filter(username='строке', username2='строка') - получение конкретного значение по двум и более значениям 
# for i in все:
# print(f'email{i.username}, username {i.username2}, пароль {i.password}', id={i.id}) - распечатка данных

# new_class = class(username='почта', username2='имя', password='пароль') - создание нового объекта
# new_class.save() - сохранение в базе данных
# или class.object.create(username='почта', username2='имя', password='пароль') - создание и запись нового объекта одной строкой

# old_class = class.objects.get(id=2) - получение объекта из класса если уверен что бдублежа быть не может напимер через id -  метод GET
# old_class.username2 = 'строка'   - изменение параметра
# old_class.save() сохранение в базе












# class.objects.get(id=2).delete() - удление 

    # class Meta:
    #     model = User
    #     fields = (
    #         'username',)
    #         'first_name',
    #         'email',)

    # def clean_password2(self):
    #     cd = self.cleaned_data
    #     if cd['password'] != cd['password2']:
    #         raise forms.ValidationError(
    #             'Passwords don\'t match.')
    #     return cd['password2']



# Create your models here.


# Создать класс для хранения "временных пользователей":
# токен, емейл, пароль, время действия
# выполнить подготовку к миграции и миграцию (создастся табличка)
# Дописать функцию, которая по токену вытаскивает всё это и "заводит" пользователя