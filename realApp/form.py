#Creating and updating models

from dataclasses import field
from inspect import formatargvalues
from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    class Meta:
        model = forum
        fields = "__all__"

class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion 
        fields ="__all__"