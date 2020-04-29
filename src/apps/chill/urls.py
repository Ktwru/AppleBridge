from django.urls import path

from .views import ChillView


urlpatterns = [
    path('chill/', ChillView.as_view()),
]
