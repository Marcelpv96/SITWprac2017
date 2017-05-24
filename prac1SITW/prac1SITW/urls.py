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
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from django.views.static import serve
from django.conf import settings

from sportsBetting.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homePage, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    # Team patterns
    url(r'^teams/list_teams/',
        TeamList.as_view(),
        name="list_teams"),
    url(r'^teams/create/$', TeamCreate.as_view(), name="create_team"),
    url(r'^teams/edit/(?P<pk>[0-9]+)$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            form_class=TeamForm,
            model=Team,
        ),
        name="edit_team"),
    url(r'^teams/delete/(?P<pk>[0-9]+)$',
        TeamLoginRequiredCheckIsOwnerDeleteView.as_view(
            template_name='delete_team_confirm.html',
            context_object_name="team",
            success_url=reverse_lazy('list_teams')
        ), name="delete_team"),
    #Competition patterns
    url(r'^competitions/list_competitions/',
        CompetitionList.as_view(),
        name="list_competitions"),
    url(r'^competitions/create/$',
        CompetitionCreate.as_view(),
        name="create_competition"),
    url(r'^competitions/edit/(?P<pk>[0-9]+)$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            form_class=CompetitionForm,
            model=Competition,
        ),
        name="edit_competition"),
    url(r'^competitions/delete/(?P<pk>[0-9]+)$',
        CompetitionLoginRequiredCheckIsOwnerDeleteView.as_view(
            template_name='delete_competition_confirm.html',
            context_object_name="competition",
            success_url=reverse_lazy('list_competitions')
        ),
        name="delete_competition"),
    # Events patterns
    url(r'^events/list_events/',
        EventList.as_view(),
        name="list_events"),
    url(r'^events/create/$', EventCreate.as_view(), name="create_event"),

    url(r'^events/(?P<id>[0-9]+)/$', list_team_events, name="list_team_events"),






    # Bets patterns
    url(r'^bets/list_bets/',
        BetsList.as_view(template_name='list_bets.html'),
        name="list_bets"),
    url(r'^bets/create/',
        BetCreate.as_view(),
        name="create_bet"),
    url(r'^bets/edit/(?P<pk>[0-9]+)',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            form_class=BetForm,
            model=Bet,
        ),
        name="edit_bet"),
    url(r'^bets/delete/(?P<pk>[0-9]+)',
        BetLoginRequiredCheckIsOwnerDeleteView.as_view(
            context_object_name='bet',
            template_name='delete_bet_confirm.html',
            success_url=reverse_lazy('list_bets')
        ),
    name="delete_bet"),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
