"""Baglan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Baglan.views import HomeView, LogoutView, RegisterView, ProfileView, EditProfileView, PostCommentView, ViewUserView
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', HomeView.as_view(), name = 'home'),
    path('admin/', admin.site.urls),
    path('post-comment/', PostCommentView.as_view(), name = 'post-comment'),
    path('user/<username>', ViewUserView.as_view(), name = 'user'),
    path('accounts/login/',	LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name = 'logout'),
    path('accounts/register/', RegisterView.as_view(), name = 'register'),
    path('accounts/profile/', ProfileView.as_view(), name = 'profile'),
    path('accounts/edit_profile/', EditProfileView.as_view(), name = 'edit_profile')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
