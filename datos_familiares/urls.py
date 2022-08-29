from django.contrib import admin
from django.urls import path
from datos_familiares.views import datos_familiares 
urlpatterns = [
    path('',datos_familiares),
]