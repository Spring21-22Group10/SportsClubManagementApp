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
from django.urls import path
#from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^expenses',views.expenses),
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
    url(r'^home_main',views.home_main),
    url(r'^home_staff',views.home_staff),
    url(r'^news',views.news),
    url(r'^tickets',views.tickets),
    url(r'^buyA',views.buyA),
    url(r'^Report',views.report),
    url(r'^matches',views.matches),
    url(r'^record_expense',views.record_expense),
    path('remove(<int:id>)',views.remove, name='remove'),
    path('add(<int:id>)',views.add, name='add'),
    url(r'^merchandise',views.merch),
    path('item(<int:id>)', views.item, name='item'),
    path('ticket(<int:id>)', views.ticket, name='ticket'),
    url(r'^past_matches',views.past_matches),
    url(r'^leagues',views.leagues),
    url(r'^addmatch',views.addmatch),
    url(r'^addmerch',views.addmerch),
    path('deletematch(<int:id>,<int:type>)', views.deletematch, name='deletematch'),
    path('editmatch(<int:id>,<int:type>)', views.editmatch, name='editmatch'),
    path('deletemerch(<int:id>)', views.deletemerch, name='deletemerch'),
    path('editmerch(<int:id>)', views.editmerch, name='editmerch'),
    path('video(<int:pk>)', views.stream_detail, name='stream_detail'),
    path('edit_expense(<int:id>)', views.edit_expense, name='edit_expense'),
    path('delete_expense(<int:id>)', views.delete_expense, name='delete_expense'),
]
