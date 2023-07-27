from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quitter.accounts'

    def ready(self):
        import quitter.accounts.signals
        result = super().ready()
        return result
