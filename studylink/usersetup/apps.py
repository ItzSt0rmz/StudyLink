from django.apps import AppConfig


class UsersetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usersetup'

    def ready(self):
        import usersetup.signals  # noqa
