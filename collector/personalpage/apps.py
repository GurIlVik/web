from django.apps import AppConfig


class PersonalpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'personalpage'
    verbose_name = 'Персональная страница' # отображение в админ панели страницы
