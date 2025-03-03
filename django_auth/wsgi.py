import os
from django.core.wsgi import get_wsgi_application

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_auth.settings')

# Get WSGI application
application = get_wsgi_application()