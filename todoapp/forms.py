# from dataclasses import fields
from django.forms import ModelForm
from todoapp.models import Todo
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["Title" , "Description" , "Date" , "Tag" , "Status"]
