from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def registerview(request):
    form= RegisterForm()
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('this is correct ')
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponse('this is wrong details ')
    return render(request, 'register.html',{'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

def loginview(request):
    form=AuthenticationForm()
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('add_user')
            else:
                messages.error(request, 'Please correct the error below.')
                return HttpResponse('this is wrong details ')
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('add_user')