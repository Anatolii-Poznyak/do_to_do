from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from organizer.forms import TaskCreationForm
from organizer.models import Task, Tag


def index(request):

    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks": tasks,
        "tags_list": tags,
    }

    return render(request, "organizer/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    # fields = "__all__"
    success_url = reverse_lazy("organizer:index")
    form_class = TaskCreationForm


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("organizer:tag-list")
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("organizer:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("organizer:tag-list")
