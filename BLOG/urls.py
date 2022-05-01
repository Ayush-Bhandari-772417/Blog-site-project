"""BLOG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication.views import registerview, change_password, loginview, logout_view
from user_profile.views import profile_detail_view, update_Profile, allUser
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adduser/', registerview, name ='add_user'),
    path('changepwd/', change_password, name='change_password'),
    path('login/', loginview, name='user_login'),
    path('logout/', logout_view, name='user_logout'),

    path('profiles/<slug:slug>/', profile_detail_view, name='profile_detail'),
    path('profiles/<slug:slug>/update', update_Profile, name='update_profile_detail'),
    path('alluser/', allUser, name ='all_data'),
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
