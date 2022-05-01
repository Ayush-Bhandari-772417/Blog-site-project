from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import Prof_Update_Form
from django.http import Http404
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def allUser(request):
    alldata = Profile.objects.all()
    return render(request, 'all_user.html',{'objec':alldata})

def profile_detail_view(request, slug=None):
    profile_obj = None
    if slug is not None:
        try:
            profile_obj = Profile.objects.get(slug=slug)
            users_det = User.objects.get(username=slug)
        except:
            raise Http404
    context = {
        "object": profile_obj,
    }
    return render(request,"profile.html",{'objs':profile_obj, 'userss':users_det})

@login_required
def update_Profile(request, slug):
    dest = Profile.objects.get(slug=slug)
    a = request.user.username
    c = f'{dest.user}'
    if a == c:
        form=Prof_Update_Form(instance=dest)
        if request.method=='POST':
            form=Prof_Update_Form(request.POST, instance=dest)
            if form.is_valid():
                form.save()
                return redirect('profile_detail')
        return render(request, 'prof_update.html',{'form':form})
    else:
        return HttpResponse('You are not the cocerned user')