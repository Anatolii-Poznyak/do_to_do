from django.shortcuts import render

from organizer.models import Task, Tag


def index(request):

    tasks = Task.objects.all()
    tags = Tag.objects.all()

    context = {
        "tasks_list": tasks,
        "tags_list": tags,

    }

    return render(request, "organizer/index.html", context=context)

