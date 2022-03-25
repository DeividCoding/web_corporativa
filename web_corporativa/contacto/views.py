from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Apartado_Contacto, MensajeRecibido

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import FormularioContacto
from django.urls import reverse_lazy
from django.template import Template,RequestContext
import procesors
from about.models import DatosEmpresa
from .models import MensajeRecibido


# Create your views here.
class Contacto(TemplateView):
    template_name="contacto/contact.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Contacto.objects.get_apartado()

        if datos:      
            context['imagenPortada']=datos.imagenPortada

        return context


# Create your views here.
class MensajeExito(TemplateView):
    template_name="contacto/exitoRegistro.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Contacto.objects.get_apartado()

        if datos:      
            context['imagenPortada']=datos.imagenPortada
            mensajeRecibido=MensajeRecibido.objects.last()

            if mensajeRecibido:
                context['mensajeRecibido']=mensajeRecibido.mensaje
            else:
                context['mensajeRecibido']="Gracias por comunicarte con nosotros enseguida una personal de la"\
                    "empresa atendera tu solicitud y se comunicara contigo."


        return context
        

class FormularioContacto(FormView):
    template_name='contacto/contact.html'
    form_class=FormularioContacto
    success_url=reverse_lazy('contacto_app:mensajeContactoExito')
    #success_url="contact/exitoRegistro.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        datos=Apartado_Contacto.objects.get_apartado()

        if datos:      
            context['imagenPortada']=datos.imagenPortada

        return context

    def form_valid(self,form):
        #nombre=self.request.POST.get('name')
        #correo=self.request.POST.get('email')
        #contenido=self.request.POST.get('content')

        # mensaje para el usuario 
        #autorSitioWeb=procesors.datos_autor.NOMBRE
        #autorSitioWeb=RequestContext(self.request,processors=[procesors.datos_autor]).get('NOMBRE')
        #print("*****************************************")

        #datosDeEmpresa=DatosEmpresa.objects.last()
        #nombreEmpresa=datosDeEmpresa.nombre
        #mensajeRecibido=MensajeRecibido.objects.last()

        #asunto=mensajeRecibido.asunto
        #mensaje="Hola: {}\n".format(nombre)
        #mensaje+=mensajeRecibido.mensaje
        #mensaje+="\n\nAtt: {}".format(nombreEmpresa)



        return super(FormularioContacto,self).form_valid(form)