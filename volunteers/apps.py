from django.apps import AppConfig


class VolunteersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'volunteers'

    def ready(self):
        # Import signals when the app is ready
        import volunteers.signals