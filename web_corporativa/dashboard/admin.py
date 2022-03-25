from django.contrib import admin
from .models import Apartado_Dashboard
from about.functions import ApartadoAdmin

# Register your models here.
admin.site.register(Apartado_Dashboard,ApartadoAdmin)
