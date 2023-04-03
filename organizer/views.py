from django.shortcuts import render
from django.views import generic

from organizer.models import Task, Tag


def index(request):

    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks": tasks,
        "tags_list": tags,
    }

    return render(request, "organizer/index.html", context=context)


class TagListview(generic.ListView):
    model = Tag
    paginate_by = 5
