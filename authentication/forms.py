from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model=User
        # fields = '__all__'
        fields=['first_name','last_name','username','email','password1']