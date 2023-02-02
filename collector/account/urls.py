from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('user/<int:user_id>/', views.personal_page,),
]


