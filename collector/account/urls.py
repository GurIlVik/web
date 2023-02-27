from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('confirmation/<email>', views.confirmation, name='confirmation'),
    # path('confirmation/<email>', views.confirmation, name='login_email'),
    path('login_email/', views.login_email, name='login_email'),
    # path('login_email_2/', views.login_email_2, name='login_email_2'),
    path('user/<int:user_id>/', views.personal_page,),
]


