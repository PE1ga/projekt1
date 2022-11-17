from django.db import models

class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class GostiSeznam(models.Model):
    Ime = models.CharField(max_length= 255)
    Agencija = models.CharField(max_length= 255)
    Cena = models.CharField(max_length= 255)
    DatumOD = models.CharField(max_length= 255)
    DatumDO = models.CharField(max_length= 255)

class Pospravljanje(models.Model):
    Soba = models.IntegerField()
    Akcija = models.CharField(max_length=20)
    Za_Oseb = models.IntegerField()
    Status = models.CharField(max_length=20)

class PospravljanjePrihodi(models.Model):
    Soba = models.IntegerField()
    St_Oseb = models.IntegerField()
    #Zahteve = models.CharField(max_length=255)
    Status = models.CharField(max_length=20)
