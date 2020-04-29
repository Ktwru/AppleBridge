
from django.contrib import admin
from django.urls import path, include

from apps.chill.urls import urlpatterns as chill_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(chill_urlpatterns)),
]
