"""website URL Configuration

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
from django.conf.urls import url
#from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index),
    url(r'^index',views.index),
    url(r'^player_login',views.player_login),
    url(r'^player_signup',views.player_signup),
    url(r'^fan_login',views.fan_login),
    url(r'^staff_login',views.staff_login),
    url(r'^forgot_password_player',views.forgot_password_player),
    url(r'^forgot_password_fan',views.forgot_password_fan),
    url(r'^forgot_password_staff',views.forgot_password_staff),
    url(r'^reset_password_player',views.reset_password_player),
    url(r'^reset_password_fan',views.reset_password_fan),
    url(r'^reset_password_staff',views.reset_password_staff),
    url(r'^home',views.home),
]
