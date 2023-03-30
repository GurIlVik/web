from django.urls import path
from . import views


urlpatterns = [
    path('<user>', views.personal_page, name='personal_page'),
]
