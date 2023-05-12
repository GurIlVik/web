from django.urls import path
from .views import *



urlpatterns = [
    path('a', index_1),
    # path('<author>/<id>', publication, name='author_publication'),

]
