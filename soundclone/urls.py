"""soundclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.track_list_view, name='index'),
    path('tracks/create', views.track_create_view, name='track-create'),
    path('tracks/<int:pk>', views.track_detail_view, name='track-detail'),
    path('tracks/<int:pk>/like', views.track_like_view, name='track-like'),
    path('tracks/<int:pk>/unlike', views.track_unlike_view, name='track-unlike'),
    path('tracks/<int:pk>/comment', views.comment_create_view, name='comment-create'),
    path('users/register', views.user_create_view, name='user-create'),
    path('users/login', auth_views.login, name='login'),
    path('users/logout', auth_views.logout, name='logout'),
    path('users/<str:username>', views.user_detail_view, name='user-detail'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
