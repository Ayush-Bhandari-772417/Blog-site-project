from django.contrib import admin
from .models import Category, BlogPost, BlogComment

# Register your models here.

admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(Viewer)