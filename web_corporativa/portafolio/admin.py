from django.contrib import admin
from .models import Categoria,Apartado_Portafolio, Proyecto
from about.functions import ApartadoAdmin


class ProyectoAdmin(admin.ModelAdmin):
    list_display=('prioridad','titulo','created','preparadoParaMostrar',)
    readonly_fields=(
        'created',
        'modified',
    )

    # ordenando del mas reciente al menos reciente
    ordering=('prioridad','created')

# Register your models here.
admin.site.register(Apartado_Portafolio,ApartadoAdmin)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Categoria)
