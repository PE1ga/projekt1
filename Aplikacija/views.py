from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.urls import reverse

# Create your views here.

def index(request):
    Ime = "Peter"

    template = loader.get_template("index.html")

    kontext = {"VstaviIme": Ime}

    return HttpResponse(template.render(kontext,request))