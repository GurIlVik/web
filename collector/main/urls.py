from django.urls import path
from .views import  main_page, publication



urlpatterns = [
    path('', main_page, name='main'),
    path('<author>/<time>', publication, name='author_publication'),

]
