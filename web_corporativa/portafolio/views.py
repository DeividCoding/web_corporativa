from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView
from django.http import Http404
from .models import Apartado_Portafolio,Proyecto,Categoria

class ProyectoDetailView(DetailView):
    model = Proyecto
    template_name = "portafolio/detalle_proyecto.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)        
        datosApartado=Apartado_Portafolio.objects.get_apartado()

        if datosApartado:   
            context['imagenPortada']=datosApartado.imagenPortada
        return context


class PortafolioEmpresa(ListView):
    model = Proyecto
    template_name = "portafolio/portafolioEmpresa.html"
    paginate_by=5

    def get_queryset(self):

        # un form manda unicamente el dato de: 'palabraClave'
        palabraClave=self.request.GET.get("palabraClave",None)
        # otro form manda unicamente el dato de: 'habilidad'
        id_categoria=self.request.GET.get("categoria",None)
        
        
        if palabraClave:
            proyectosConDichaPalabra=Proyecto.objects.filter(
                titulo__icontains=palabraClave,preparadoParaMostrar=True
            ).order_by('created')

            return proyectosConDichaPalabra

        elif id_categoria:
            try:
                id_categoria=int(id_categoria)
                categoria=Categoria.objects.get(id=id_categoria)
                # haciendo uso del related name para hallar todos los cursos que pertenezcan a dicha categoria...
                proyectosConDichaCategoria=categoria.get_proyectos.all().filter(preparadoParaMostrar=True).order_by('created')
                return proyectosConDichaCategoria
            except:
                return Proyecto.objects.none()
        else:
            datos=Proyecto.objects.all().filter(preparadoParaMostrar=True).order_by('created')
            return datos



    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)        
        datosApartado=Apartado_Portafolio.objects.get_apartado()


        # un form manda unicamente el dato de: 'palabraClave'
        palabraClave=self.request.GET.get("palabraClave",None)
        # otro form manda unicamente el dato de: 'habilidad'
        id_categoria=self.request.GET.get("categoria",None)
        
        
        if palabraClave:
            context['palabraClave_DIO_USER']=palabraClave

        elif id_categoria:
            context['id_categoria_DIO_USER']=int(id_categoria)


        if datosApartado:   
            context['imagenPortada']=datosApartado.imagenPortada
            context['frasePortafolio']=datosApartado.frasePortafolio
            # solo retornara los primeros 3 de cada uno...
            context['articulosDestacados']=datosApartado.proyectosDestacados.all().filter(preparadoParaMostrar=True).order_by('created')[:3]    
            context['articulosRecientes']=Proyecto.objects.filter(preparadoParaMostrar=True).order_by('created')[:3]
            context['categorias']=Categoria.objects.all()

        return context


###############################################################################################################################################
# API  CON DJANGO REST FRAMEWORK
###############################################################################################################################################


from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,CreateAPIView,RetrieveAPIView,
    DestroyAPIView,RetrieveUpdateAPIView
    )

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    Categoria_editarCrearEliminar_Serializer, Categoria_info_Serializer, Proyecto_info_Serializer,Proyecto_crearEditar_Serializer,Proyecto_eliminar_Serializer,
    )
    



class ProyetoListApiView(ListAPIView):

    serializer_class=Proyecto_info_Serializer

    def get_queryset(self):
        '''
        Nos retornara la lista de resultados particulares que
        cumplan con el filtro
        '''

        return Proyecto.objects.all()
        
        #kword=self.kwargs['kword']
        #return Person.objects.filter(
        #    full_name__icontains=kword
        #)


class ProyectoCreateApiView(CreateAPIView):
    serializer_class=Proyecto_crearEditar_Serializer

class ProyectoUpdateApiView(RetrieveUpdateAPIView):
    serializer_class=Proyecto_info_Serializer
    # indicandole donde buscar
    queryset=Proyecto.objects.all()

class ProyectoDetailApiView(RetrieveAPIView):
    serializer_class=Proyecto_info_Serializer
    # indicandole donde buscar
    queryset=Proyecto.objects.all()


class ProyectoDeleteApiView(DestroyAPIView):
    serializer_class=Proyecto_eliminar_Serializer
    # indicandole donde buscar
    queryset=Proyecto.objects.all()









class DarLike_ApiView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, *args, **kwargs):
        idProyecto=self.kwargs['pk']
        estatus=None
        try:
            proyectoPopular=Proyecto.objects.get(id=idProyecto)
            likesAntes=proyectoPopular.likes
            print("**************************************")
            print(likesAntes)
            proyectoPopular.likes=proyectoPopular.likes+1
            likesDespues=proyectoPopular.likes
            print("**************************************")
            print(likesDespues)
            proyectoPopular.save()
            estatus="Exito al registrar like, likes antes: {} likes ahora: {}".format(likesAntes,likesDespues)
        except:
            estatus="Error al registrar like"
    
        return  Response(
            {
                'estatus':estatus
            }
        )


class DarDislike_ApiView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, *args, **kwargs):
        idProyecto=self.kwargs['pk']
        estatus=None
        try:
            proyectoPopular=Proyecto.objects.get(id=idProyecto)
            likesAntes=proyectoPopular.likes
            print("**************************************")
            print(likesAntes)

            if proyectoPopular.likes>0:
                proyectoPopular.likes=proyectoPopular.likes-1
                likesDespues=proyectoPopular.likes
                print("**************************************")
                print(likesDespues)
                proyectoPopular.save()
            estatus="Exito al registrar dislikes, likes antes: {} likes ahora: {}".format(likesAntes,likesDespues)
        except:
            estatus="Error al registrar like"
    
        return  Response(
            {
                'estatus':estatus
            }
        )




class VisitarProyecto_ApiView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, *args, **kwargs):
        idProyecto=self.kwargs['pk']
        estatus=None
        try:
            proyectoPopular=Proyecto.objects.get(id=idProyecto)
            visitasAntes=proyectoPopular.visitas

            proyectoPopular.visitas=proyectoPopular.visitas+1
            visitasDespues=proyectoPopular.visitas

            proyectoPopular.save()
            estatus="Exito al registrar visita, visitas antes: {} visitas ahora: {}".format(visitasAntes,visitasDespues)
        except:
            estatus="Error al registrar visita"
    
        return  Response(
            {
                'estatus':estatus
            }
        )



#############################
# categorias.




class CategoriaListApiView(ListAPIView):

    serializer_class=Categoria_info_Serializer

    def get_queryset(self):
        '''
        Nos retornara la lista de resultados particulares que
        cumplan con el filtro
        '''

        return Categoria.objects.all()
        
        #kword=self.kwargs['kword']
        #return Person.objects.filter(
        #    full_name__icontains=kword
        #)

class CategoriaCreateApiView(CreateAPIView):
    serializer_class=Categoria_editarCrearEliminar_Serializer

class CategoriaUpdateApiView(RetrieveUpdateAPIView):
    serializer_class=Categoria_editarCrearEliminar_Serializer
    # indicandole donde buscar
    queryset=Categoria.objects.all()
