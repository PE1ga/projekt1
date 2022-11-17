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

def TabelaPokazi(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template("tabela.html")
    context = {"MyMembers" : mymembers,}

    return HttpResponse(template.render(context, request))

def SeznamGOSTI(request):
    gosti = GostiSeznam.objects.all().values()
    template = loader.get_template("SeznamGostov.html")
    context = {"GostiSeznam":gosti,}

    return HttpResponse(template.render(context, request))

def update(request, id):
    gost = GostiSeznam.objects.get(id=id)
    template = loader.get_template("update.html")
    context = {"Gost": gost}

    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    ime = request.POST["Ime"]
    agencija = request.POST["Agencija"]
    cena = request.POST["Cena"]
    datumOD = request.POST["DatumOD"]
    datumDO = request.POST["DatumDO"]
    
    record = GostiSeznam.objects.get(id=id)
    record.Ime = ime
    record.Agencija = agencija
    record.Cena = cena
    record.DatumOD = datumOD
    record.DatumDO = datumDO
   
    record.save()

    return HttpResponseRedirect(reverse("SeznamGostov"))


def PospravljanjeSob(request):
    sobe = Pospravljanje.objects.all().values()
    StSob = Pospravljanje.objects.all().count() - Pospravljanje.objects.filter(Status = "OK").count()
    template = loader.get_template("pospravljanje.html")
    context = {"SobeSeznam":sobe, "STSOB": StSob}

    return HttpResponse(template.render(context, request))


def PotrdiCiscenje(request, id):
    record = Pospravljanje.objects.get(id=id)
    record.Status = "OK"
    record.save()

    return HttpResponseRedirect(reverse("Pospravljanje"))

def ResetCiscenje(request, id):
    record = Pospravljanje.objects.get(id=id)
    record.Status = ""
    record.save()

    return HttpResponseRedirect(reverse("Pospravljanje"))

def PosprPrihodi(request):
    Sobe = PospravljanjePrihodi.objects.all().values()
    
    StSob = PospravljanjePrihodi.objects.all().count() - PospravljanjePrihodi.objects.filter(Status = "OK").count()               
    
    template = loader.get_template("pospr_prihodi.html")
    context = {"SobeSeznam": Sobe,"STSOB": StSob}
    return HttpResponse(template.render(context, request))

def PotrdiCiscenjePrh(request, id):
    record = PospravljanjePrihodi.objects.get(id=id)
    record.Status = "OK"
    record.save()

    return HttpResponseRedirect(reverse("Pospravljanje_Prihodi"))

def ResetCiscenjePrh(request, id):
    record = PospravljanjePrihodi.objects.get(id=id)
    record.Status = ""
    record.save()

    return HttpResponseRedirect(reverse("Pospravljanje_Prihodi"))