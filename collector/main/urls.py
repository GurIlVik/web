from django.urls import path
from .views import  main_page


urlpatterns = [
    path('', main_page),
    # path('', main_page, name='index'),
]