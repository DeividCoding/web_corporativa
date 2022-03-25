from django.contrib import admin
from .models import Apartado_Contacto,MensajeRecibido,RedCotacto
from about.functions import ApartadoAdmin

# Register your models here.
admin.site.register(Apartado_Contacto,ApartadoAdmin)
admin.site.register(MensajeRecibido)
admin.site.register(RedCotacto)
