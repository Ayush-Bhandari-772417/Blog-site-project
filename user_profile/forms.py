from django.db import models
from django.forms import fields
from django import forms
from .models import Profile

class Prof_Update_Form(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'