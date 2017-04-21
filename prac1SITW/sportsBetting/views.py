# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context_processors import csrf
from django.template import Context
# Create your views here.


def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content": "Estàs a sports betiitng."})

    page = template.render(var)
    return HttpResponse(page)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)


def profile(request):
    return render_to_response('registration/profile.html')


def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
