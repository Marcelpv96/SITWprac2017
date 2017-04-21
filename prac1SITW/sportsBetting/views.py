# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404

from django.template import Context
from django.template.loader import get_template

from django.contrib.auth.models import User

# Create your views here.
def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content" : "Estàs a sports betiitng."})

    page = template.render(var)
    return HttpResponse(page)
