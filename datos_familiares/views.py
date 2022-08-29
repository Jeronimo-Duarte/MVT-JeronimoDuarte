from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from datos_familiares.models import Familiar
# Create your views here.

def datos_familiares(request):
    familiares= Familiar.objects.all()
    diccionario= {'familiar':familiares}
    plantilla= loader.get_template("template_1.html")
    documento_html= plantilla.render(diccionario)
    return HttpResponse(documento_html)
