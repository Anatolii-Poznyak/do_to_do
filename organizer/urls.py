from django.urls import path
from organizer.views import index
from .views import TagListview


urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListview.as_view(), name="tag-list")
]

app_name = "organizer"
