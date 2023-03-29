from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('<user>', views.personal_page, name='individ_page'),
    # path('confirmation/<user>', views.confirmation, name='confirmation'),
    path('login_email/', views.login_email, name='login_email'),
    path('logout/', views.logout_view, name='logout'), 
    path('user/<int:user_id>/', views.personal_page,),
]


