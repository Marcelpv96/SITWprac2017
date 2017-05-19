# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView

from Betfair.BetfairClient import getEventsforTeam

from models import Team, Event, Sport, Bet
from forms import TeamForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content": "Estàs a sports betiitng.",
                   'user': request.user})

    page = template.render(var)
    return HttpResponse(page)


############################### TEAMS VIEWS ############################################################
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(request=request)
            return redirect('team_correctly')
    else:
        form = TeamForm()

    return render(request, 'add_team.html', {
        'form': form
    })

def edit_team(request, id):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=Team.objects.get(id=id))
        if form.is_valid():
            form.save(request=request)
            return redirect('team_correctly')
    else:
        form = TeamForm(instance=Team.objects.get(id=id))

    return render(request, 'add_team.html', {
        'form': form
    })

def team_remove(request, id):
    tmp = Team.objects.get(id=id)
    Team.objects.get(id=id).delete()

    return render(request, 'remove_team.html', { 'team': tmp })

def team_correctly(request):
    return render (request, 'team_correctly.html')

def list_teams(request):
    teams_list = Team.objects.all().order_by('name')

    if request.method == 'GET':
        search_query = request.GET.get('search_box', default=None)
        if search_query:
            teams_list = Team.objects.filter(name__contains=search_query).order_by('name')

    paginator = Paginator(teams_list, 20)

    page = request.GET.get('page')
    try:
        teams = paginator.page(page)
    except PageNotAnInteger:
        teams = paginator.page(1)
    except EmptyPage:
        teams = paginator.page(paginator.num_pages)

    return render(request, 'list_teams.html', {'user':request.user, 'teams': teams, 'query': search_query})

def list_team_events(request, id):
    # TODO: Api call
    team = Team.objects.get(id=id).short_name
    print id
    #for event in events:
    event = Event.objects.filter(Q(team1__id__exact=id) | Q(team2__id__exact=id))

    return render(request, 'list_team_events.html', {'content': 'Api call de ' + team, 'events': event})


################################### BETS VIEWS #########################################
# Implemented with simple security, later on I will upgrade this
def login_error(request):
    return render(request, 'error_login_bets.html')


class BetsList(ListView):
    model = Bet

    def get_context_data(self, **kwargs):
        context = super(BetsList, self).get_context_data(**kwargs)
        context['bets'] = Bet.objects.filter(user__username__exact=self.request.user.username)
        return context
