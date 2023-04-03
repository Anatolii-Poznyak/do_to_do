from django.urls import path
from organizer.views import index, TaskCreateView
from .views import TagListView


urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create")
]

app_name = "organizer"
