from django.urls import path
from .views import *



urlpatterns = [
    path('a', index_1),
    path('b', index_2),
    path('с', index_3),
    path('d', index_4),
    path('e', index_5),
    
    # path('<author>/<id>', publication, name='author_publication'),

]
