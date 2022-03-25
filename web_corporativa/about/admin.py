from django.contrib import admin
from .models import DatosEmpresa,Apartado_About

from about.functions import ApartadoAdmin



# Register your models here.

admin.site.register(DatosEmpresa)
admin.site.register(Apartado_About,ApartadoAdmin)
