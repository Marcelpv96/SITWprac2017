# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, redirect
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Betfair.BetfairClient import getEventsforTeam

from models import Team, Event, Sport, Bet
from forms import TeamForm, BetForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


############################ SECURITY ######################################

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if type(obj) is Team:
            if not obj.created_by == self.request.user:
                raise PermissionDenied
            return obj

        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class BetLoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Bet

class BetLoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Bet

class TeamLoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    model = Team

class TeamLoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Team

def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content": "Estàs a sports betiitng.",
                   'user': request.user})

    page = template.render(var)
    return HttpResponse(page)


############################### TEAMS VIEWS ############################################################
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Bet
    template_name = 'create_bet.html'
    form_class = TeamForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # If an objects already exists, delete the old one and override it
        if Team.objects.filter(name=form.instance.name, short_name=form.instance.short_name).exists():
            Team.objects.filter(name=form.instance.name, short_name=form.instance.short_name).delete()

        return super(TeamCreate, self).form_valid(form)

class TeamList(ListView):
    model = Team
    template_name = 'list_teams.html'


    def get_context_data(self, **kwargs):
        context = super(TeamList, self).get_context_data(**kwargs)

        context['teams'] = Team.objects.all()
        context['user'] = self.request.user

        query = self.request.GET.get('search_box', default=None)

        if query:
            context['teams'] = Team.objects.filter(name__contains=query)
            context['query'] = query

        return context

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
class BetsList(LoginRequiredMixin, ListView):
    model = Bet

    def get_context_data(self, **kwargs):
        context = super(BetsList, self).get_context_data(**kwargs)
        context['bets'] = Bet.objects.filter(user__username__exact=self.request.user.username)
        return context


class BetCreate(LoginRequiredMixin, CreateView):
    model = Bet
    template_name = 'create_bet.html'
    form_class = BetForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        # If an objects already exists, delete the old one and override it
        if Bet.objects.filter(event=form.instance.event, description=form.instance.description).exists():
            Bet.objects.filter(event=form.instance.event, description=form.instance.description).delete()

        return super(BetCreate, self).form_valid(form)
