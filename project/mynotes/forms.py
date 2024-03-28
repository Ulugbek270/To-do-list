from django.forms import Textarea, TextInput, CheckboxInput
from .models import Task
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']

        widgets = {
            'title': TextInput(attrs={

                'class': 'form-control',
                'placeholder': 'Name'

            }),
            'description': Textarea(attrs={

                'class': 'form-control',
                'placeholder': 'Description'

            }),
            'complete': CheckboxInput(attrs={
                'class': 'form-check-input',
            })
        }


