from django.urls import path
from django.urls.resolvers import URLPattern
from .import views


urlpatterns = [
    path("creditos/",views.allCredit, name="creditos"),
    path("creditos/<int:ids>/",views.oneCreditbyid, name="creditosid"),
    path("creditos/add/",views.CrearCredito, name="creditos"),
    path("creditos/update/<str:ids>/",views.updateCredito, name="creditosupdate"),
    path("creditos/delete/<str:ids>/",views.deleteCredito, name="creditosdelete"),
    path("puntuacion/",views.allpuntacion, name="puntuacion"),
    path("user/<str:ids>/",views.userData, name="usersid"),

    
    
]