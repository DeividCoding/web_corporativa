from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Apartado_Dashboard
from portafolio.models import Proyecto

# Create your views here.
#class DashBoard_Inicio(TemplateView):
#    template_name="dashboard/visitas.html"
#
#    def get_context_data(self,**kwargs):
#        context=super().get_context_data(**kwargs)
#        datos=Apartado_Dashboard.objects.get_apartado()
#
#        if datos:      
#            context['imagenPortada']=datos.imagenPortada
#
#        return context






class DashBoard_Inicio(ListView):
    model = Proyecto
    template_name = "dashboard/visitas.html"
    paginate_by=5

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)        
        datosApartado=Apartado_Dashboard.objects.get_apartado()

        if datosApartado:      
            context['imagenPortada']=datosApartado.imagenPortada

        #  href="?page={{ page_obj.previous_page_number }}&categoria={{id_categoria_DIO_USER}}"

        proyectoA_mostrar=None
        id_proyecto=self.request.GET.get("idProyecto",None)
        if id_proyecto:
            try:
                id_proyecto=int(id_proyecto)
                proyectoA_mostrar=Proyecto.objects.get(id=id_proyecto)
            except:
                pass
        
        if proyectoA_mostrar:
            context['proyectoA_mostrar']=proyectoA_mostrar

        return context
