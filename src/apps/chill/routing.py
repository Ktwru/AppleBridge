from django.urls import re_path
from apps.chill import consumers

websocket_urlpatterns = [
    re_path(r'ws/chill/(?P<room_id>\w+)/$', consumers.ChillConsumer),
]
