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

from models import *
from forms import *
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

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'form.html'

    def get_context_data(self, **kwargs):
        context = super(LoginRequiredCheckIsOwnerUpdateView,self).get_context_data(**kwargs)
        context['model'] = self.model.__name__
        return context

class BetLoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Bet

class TeamLoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Team

class CompetitionLoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = Competition

def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content": "Estàs a sports betiitng.",
                   'user': request.user})

    page = template.render(var)
    return HttpResponse(page)


############################### TEAMS VIEWS ############################################################
# Make a list of objects paginated
def pagination(request, item_list, elems_per_page):
    paginator = Paginator(item_list, elems_per_page)

    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects

class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    template_name = 'form.html'
    form_class = TeamForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # If an objects already exists, delete the old one and override it
        if Team.objects.filter(name=form.instance.name, short_name=form.instance.short_name).exists():
            Team.objects.filter(name=form.instance.name, short_name=form.instance.short_name).delete()

        return super(TeamCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TeamCreate, self).get_context_data(**kwargs)
        context['model'] = 'Team'
        return context


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

        context['teams'] = pagination(self.request, context['teams'], 10)

        return context


def list_team_events(request, id):
    # TODO: Api call
    team = Team.objects.get(id=id).short_name
    print id
    #for event in events:
    event = Event.objects.filter(Q(team1__id__exact=id) | Q(team2__id__exact=id))

    return render(request, 'list_team_events.html', {'content': 'Api call de ' + team, 'events': event})

################################### COMPETITION VIEWS ################################
class CompetitionList(ListView):
        model = Competition
        template_name = 'list_competitions.html'

        def get_context_data(self, **kwargs):
            context = super(CompetitionList, self).get_context_data(**kwargs)

            context['competitions'] = Competition.objects.all()
            context['user'] = self.request.user

            query = self.request.GET.get('search_box', default=None)

            if query:
                context['competitions'] = Competition.objects.filter(name__contains=query)
                context['query'] = query

            context['competitions'] = pagination(self.request, context['competitions'], 10)

            return context

class CompetitionCreate(LoginRequiredMixin, CreateView):
    model = Competition
    template_name = 'form.html'
    form_class = CompetitionForm

    def get_context_data(self, **kwargs):
        context = super(CompetitionCreate, self).get_context_data(**kwargs)
        context['model'] = 'Competition'
        return context


    def form_valid(self, form):
        form.instance.user = self.request.user

        # If an objects already exists, delete the old one and override it
        if Competition.objects.filter(name=form.instance.name, short_name=form.instance.short_name).exists():
            Competition.objects.filter(name=form.instance.name, short_name=form.instance.short_name).delete()

        return super(CompetitionCreate, self).form_valid(form)


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
    template_name = 'form.html'
    form_class = BetForm

    def form_valid(self, form):
        form.instance.user = self.request.user

        # If an objects already exists, delete the old one and override it
        if Bet.objects.filter(event=form.instance.event, description=form.instance.description).exists():
            Bet.objects.filter(event=form.instance.event, description=form.instance.description).delete()

        return super(BetCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BetCreate, self).get_context_data(**kwargs)
        context['model'] = 'Bet'
        return context
