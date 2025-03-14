"""
WSGI config for nagarik_sahayata project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Ensure the correct settings module is used
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nagarik_sahayata.settings')

application = get_wsgi_application()