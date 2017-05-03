# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
# Create your views here.


def homePage(request):
    template = get_template("homepage.html")
    var = Context({"content": "Estàs a sports betiitng.",
                   'user': request.user})

    page = template.render(var)
    return HttpResponse(page)
