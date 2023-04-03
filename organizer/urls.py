from django.urls import path
from organizer.views import index, TaskCreateView, TagCreateView, TagUpdateView
from .views import TagListView


urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "organizer"
