from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Category, BlogPost, BlogComment
from .forms import Category_Add_Form, Blog_Post_Form, Blog_Comment_Form, Blog_Update_Form

# Create your views here.

@login_required
def add_Category(request):
    form = Category_Add_Form()
    if request.method == 'POST':
        form = Category_Add_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your required category is added ')
        else:
            messages.error(request, 'Please correct the error below.')
    return render(request, 'add_category.html',{'form':form})

@login_required
def blog_post(request):
    form = Blog_Post_Form()
    if request.method == 'POST':
        form = Blog_Post_Form(request.POST or None, request.FILES or None, instance=dest)
        if form.is_valid():
            form.save()
            return HttpResponse('Your new blog is created ')
        else:
            messages.error(request, 'Please correct the error below.')
    return render(request, 'add_category.html',{'form':form})

@login_required
def blog_comment(request):
    form = Blog_Comment_Form()
    if request.method == 'POST':
        form = Blog_Comment_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your new comment for the blog is created ')
    return render(request, 'add_category.html',{'form':form})

@login_required
def update_Blog(request, slug):
    dest = BlogPost.objects.get(slug=slug)
    a = request.user.username
    c = f'{dest.author}'
    if a == c:
        form=Blog_Update_Form(instance=dest)
        if request.method=='POST':
            form=Blog_Update_Form(request.POST or None, request.FILES or None, instance=dest)
            if form.is_valid():
                form.save()
                return redirect('login')
        return render(request, 'add_category.html',{'form':form})
    else:
        return HttpResponse('You are not the author of this blog')