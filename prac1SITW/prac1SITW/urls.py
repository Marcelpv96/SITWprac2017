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

from django.views.static import serve
from django.conf import settings

from sportsBetting.views import *
from rest_framework.urlpatterns import format_suffix_patterns
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
    # Competition patterns
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
    url(r'^events/list_events/(?P<pk>[0-9]*)$',
        EventList.as_view(),
        name="list_events"),
    url(r'^events/create/$', EventCreate.as_view(), name="create_event"),
    url(r'^events/delete/(?P<pk>[0-9]+)/$',
        EventLoginRequiredCheckIsOwnerDeleteView.as_view(
            context_object_name='event',
            template_name='delete_event_confirm.html',
            success_url='/events/list_events'
        ), name="delete_event"),
    # Bets patterns
    url(r'^bets/list_bets/',
        BetsList.as_view(template_name='list_bets.html'),
        name="list_bets"),
    url(r'^bets/create/(?P<event_id>[0-9]*)$',
        BetCreate.as_view(),
        name="create_bet"),
    url(r'^bets/edit/(?P<pk>[0-9]+)$',
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
urlpatterns += [
     url(r'^api/competitions/$',
        APICompetitionList.as_view(), name='competition-list'),
     url(r'^api/teams/$',
        APITeamList.as_view(), name='teams-list'),
     url(r'^api/events/$',
        APIEventList.as_view(), name='events-list'),
     url(r'^api/bets/$',
        APIBetList.as_view(), name='bets-list'),
]

#curl -H 'Accept: application/json' -u admin:1234 http://127.0.0.1:8000/api/events/

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
