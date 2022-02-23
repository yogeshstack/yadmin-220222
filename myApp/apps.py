from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myApp'
    # This function is the only new thing in this file
    # it just imports the signal file when the app is ready
    def ready(self):
        import myApp.signals
