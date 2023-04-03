from django.urls import path
from organizer.views import index


urlpatterns = [
    path("", index, name="index"),
]