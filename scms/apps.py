from django.apps import AppConfig

class ScmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scms'

    def ready(self):
        import scms.signals  # Ensure signals are loaded when the app starts
