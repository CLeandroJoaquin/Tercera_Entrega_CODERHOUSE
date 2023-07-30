from django.urls import include, path
from django.contrib import admin
from Personal import views
from Personal.views import inicio
urlpatterns = [
    path("",inicio, name="inicio"),
    path("personal", views.lista_personal,name="Personal"),
    
    
]