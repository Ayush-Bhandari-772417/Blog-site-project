from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from user_profile.models import Profile
from .models import Category, BlogPost, BlogComment
from .forms import Category_Add_Form, Blog_Post_Form, Blog_Comment_Form, Blog_Update_Form

# Create your views here.

def allBlog(request):
    alldata = BlogPost.objects.all()
    return render(request, 'all_blog.html',{'objec':alldata})

def detail_blog_view(request, slug=None):
    blog_obj = None
    # profile_obj = None
    if slug is not None:
        try:
            blog_obj = Blog.objects.get(slug=slug)
            blog_obj.view = blog_obj + 1
            form.save()
        except:
            raise Http404
    # context = {
    #     "object": blog_obj,
    # }
    return render(request,"detail_blog.html",{'objs':blog_obj})

@login_required
def add_Category(request):
    form = Category_Add_Form()
    if request.method == 'POST':
        form = Category_Add_Form(request.POST, request.FILES)
        if form.is_valid():
            Job = form.save(commit=False)
            Job.adder = request.user
            Job.save()
            prof = Profile.objects.get(slug=request.user)
            prof.no_of_activities = prof.no_of_activities + 1
            prof.no_of_new_category = prof.no_of_new_category + 1
            prof.save()
            return HttpResponse('Your required category is added ')
        else:
            messages.error(request, 'Please correct the error below.')
    return render(request, 'add_category.html',{'form':form})

@login_required
def blog_post(request):
    form=Blog_Post_Form()
    if request.method=='POST':
        form = Blog_Post_Form(request.POST, request.FILES)
        if form.is_valid():
            Job = form.save(commit=False)
            Job.author = request.user
            Job.save()
            prof = Profile.objects.get(slug=request.user)
            prof.no_of_activities = prof.no_of_activities + 1
            prof.no_of_blog = prof.no_of_blog + 1
            prof.save()
            return HttpResponse('Your new blog is created ')
            return redirect('all_data')
        else:
            messages.error(request, 'Please correct the error below.')
    return render(request, 'add_blog.html',{'form':form})

@login_required
def blog_comment(request, slug = None):
    form = Blog_Comment_Form()
    if request.method == 'POST':
        form = Blog_Comment_Form(request.POST or None, request.FILES or None, instance=dest)
        if form.is_valid():
            Job = form.save(commit=False)
            Job.commentor = request.user
            Job.save()
            dest = BlogPost.objects.get(slug=slug)
            dest.count_comments = dest.count_comments + 1
            dest.save()
            prof = Profile.objects.get(slug=request.user)
            prof.no_of_activities = prof.no_of_activities + 1
            prof.no_of_comments = prof.no_of_comments + 1
            prof.save()
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


def LikeView(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('full_blog', args=[str(pk)]))