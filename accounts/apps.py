from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

#bu yozilgan va signals import qilingan
    def ready(self):
        import accounts.signals
