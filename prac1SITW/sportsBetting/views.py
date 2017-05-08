# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render

from models import Team

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content": "Estàs a sports betiitng.",
                   'user': request.user})

    page = template.render(var)
    return HttpResponse(page)


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

    return render(request, 'list_teams.html', {'teams': teams, 'query': search_query})
