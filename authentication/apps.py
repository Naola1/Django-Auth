from django.apps import AppConfig

class AuthenticationConfig(AppConfig):
    """
    Django app configuration for authentication
    - Sets default auto field type
    - Initializes signals when app is ready
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
    
    def ready(self):
        """
        Import signals when application is loaded
        """
        import authentication.signals
