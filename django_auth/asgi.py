import os
from django.core.asgi import get_asgi_application

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auth.settings')

# Get ASGI application
application = get_asgi_application()
