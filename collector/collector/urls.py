from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from start.views import page_not_found
from collector import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('start.urls')),
    path('main/', include('main.urls')),
    path('personalpage/', include('personalpage.urls')),
    path('presentation/', include('presentation.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler404 = page_not_found
# так же есть  
# handler403 - доступ запрещен
# handler500 - ошибка сервера
# handler400 - невозможно обработать запрос
# так же во Вью можно импортировать Http404() и через raise Http404() - перенаправить 
# запрос нежелательного потльзователя или нежелательный запрос с ошибкой
# https://www.youtube.com/watch?v=af7KvkQORwo&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=3 - 18 минута


# redirect('/', permanent=True) - для перенаправления по редиректу на постоянной основе.
# для редиректов лучше применять имя дороги 