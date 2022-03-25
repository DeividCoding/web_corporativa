from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import Apartado_About
from django.http import HttpResponse,Http404, response
from django.http import FileResponse
import os


class About(TemplateView):
    template_name="about/about.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_About.objects.get_apartado()

        if datos:
            context['imagenPortada']=datos.imagenPortada
            context['descripccion']=datos.descripccion
            context['foto']=datos.foto
        return context