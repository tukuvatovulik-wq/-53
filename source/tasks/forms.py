from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["description", "details", "status", "due_date"]
        widgets = {
            "details": forms.Textarea(attrs={"rows": 5}),
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }
