from django.db import models
from django.forms import fields
from django import forms
from .models import Category, BlogPost, BlogComment

class Category_Add_Form(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class Blog_Comment_Form(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = '__all__'

class Blog_Update_Form(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
