"""prac1SITW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.views.static import serve
from django.conf import settings

from sportsBetting.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homePage, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^teams/list_teams/', list_teams, name="list_teams"),
    url(r'^teams/add_team/$', add_team, name="add_team"),
    url(r'^teams/edit_team/(?P<id>[0-9]+)$', edit_team, name="edit_team"),
    url(r'^teams/correctly/$', team_correctly, name="team_correctly"),
    url(r'^teams/delete/(?P<id>[0-9]+)$', team_remove, name="team_remove"),
    url(r'^events/(?P<id>[0-9]+)/$', list_team_events, name="list_team_events"),
    url(r'^bets/list_bets/', BetsList.as_view(template_name='list_bets.html'), name="list_bets"),
    url(r'^bets/login_error/', login_error, name="login_error"),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
