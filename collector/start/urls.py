from django.urls import path
from . import views


urlpatterns = [
    path('', views.privet, name='start'), 
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('login_email/', views.login_email, name='login_email'),
    path('logout/', views.logout_view, name='logout'), 
]


