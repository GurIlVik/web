from django.contrib import admin
from .models import UserTemporaryModels, UserTemporaryToken

admin.site.register(UserTemporaryModels)
admin.site.register(UserTemporaryToken)