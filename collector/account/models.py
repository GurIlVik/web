# coding: utf-8
from django.db import models


class UserTemporaryModels():
    self.token = ''
    self.username = ''
    self.password =''
    self.time = ''
    self.username2 = ''


# Create your models here.


# Создать класс для хранения "временных пользователей":
# токен, емейл, пароль, время действия
# выполнить подготовку к миграции и миграцию (создастся табличка)
# Дописать функцию, которая по токену вытаскивает всё это и "заводит" пользователя