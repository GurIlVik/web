from django.urls import path
from . import views


urlpatterns = [
    path('<user>', views.personal_page, name='personal_page'),
    path('<user>/reception', views.personal_page_reception,),
    path('<user>/mistake', views.personal_page_mistake,),
    path('<user>/block_page', views.personal_block_page,),
]
