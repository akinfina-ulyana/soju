"""
ASGI config for soju project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import dialogues.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "soju.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket':AuthMiddlewareStack(
        URLRouter(
            dialogues.routing.websocket_urlpatterns
        )
    )
})
