from django.apps import AppConfig

# здесь происходит настройка и конфигурация конкретного приложения
class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
