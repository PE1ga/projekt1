from django.urls import path
from . import views

urlpatterns = [
    path(route="", view = views.index, name="PrviTest"),
    path(route= "tabelaPrikaz/", view=views.TabelaPokazi, name="TabelaPrikaz"),
    path(route= "seznam_gostov/", view= views.SeznamGOSTI, name="SeznamGostov"),
    path(route= "seznam_gostov/update/<int:id>", view= views.update, name="update"),
    path(route= "seznam_gostov/update/updaterecord/<int:id>", view= views.updaterecord, name="updaterecord"), 
    
    # Odhodi, menjave, pospravljanje
    path(route="pospravljanje/", view= views.PospravljanjeSob, name="Pospravljanje"),   
    path(route="pospravljanje/confirm/<int:id>", view=views.PotrdiCiscenje, name="PotrdiCiscenje"),
    path(route="pospravljanje/reset/<int:id>", view=views.ResetCiscenje, name="ResetCiscenje"),
    
    # Prihodi
    path(route="pospravljanje/pospravljanje_prihodi/", view = views.PosprPrihodi, name="Pospravljanje_Prihodi"),
    path(route="pospravljanje/pospravljanje_prihodi/confirm/<int:id>", view=views.PotrdiCiscenjePrh, name="PotrdiCiscenjeP"),
    path(route="pospravljanje/pospravljanje_prihodi/reset/<int:id>", view=views.ResetCiscenjePrh, name="ResetCiscenjeP"),
    
    
    
    ]



                