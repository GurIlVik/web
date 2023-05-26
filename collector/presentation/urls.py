from django.urls import path
from .views import *



urlpatterns = [
    path('a', index_1),
    path('b', index_2),
    path('с', index_3),
    path('d', index_4),
    path('e', index_5),
    path('f', index_6),
    path('g', index_7),
    
    
    # path('<author>/<id>', publication, name='author_publication'),

]
