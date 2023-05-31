from django.apps import AppConfig


class MultiAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'multi_app'
