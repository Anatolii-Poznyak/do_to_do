from django import forms

from organizer.models import Task


class TaskCreationForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Task.tags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
