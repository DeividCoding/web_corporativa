from django.db import models

# Create your models here.
from django.db import models
from about.functions import Apartado
from model_utils.models import TimeStampedModel

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(verbose_name="Nombre de la categoria",max_length=150)

    def __str__(self):
        return self.nombre

class Proyecto(TimeStampedModel):

    SATISFACCION_CLIENTE={
        '1':"1 estrella  (mala)",
        '2':"2 estrellas (insatisfecho)",
        '3':"3 estrellas (regular)",
        '4':"4 estrellas (bueno)",
        '5':"5 estrellas (excelente)",
    }



    preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)
    calificacionCliente=models.CharField(
        verbose_name="Satisfaccion del cliente",
        max_length=1,
        choices=tuple(SATISFACCION_CLIENTE.items()),
        default='1'
    )
    likes=models.IntegerField(verbose_name="Likes recibidos",default=0)
    visitas=models.IntegerField(verbose_name="visitas recibidas",default=0)

    titulo=models.CharField(verbose_name="Titulo",max_length=150)
    imagen=models.ImageField(verbose_name="Imagen del proyecto",upload_to="imagenes_de_proyectos")    
    prioridad=models.PositiveSmallIntegerField(verbose_name="Prioridad de aparicion",default=0)
    categorias=models.ManyToManyField(Categoria,related_name="get_proyectos")
    descripccion=models.TextField(verbose_name="Breve descripccion del proyecto:",default="",null=True)
    contenido=models.TextField(verbose_name="Descripccion mas extensa de lo que que trata el proyecto",default="")

    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"

        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']

    def __str__(self):
        return "Proyecto: {}".format(self.titulo)

class Apartado_Portafolio(Apartado):
    proyectosDestacados=models.ManyToManyField(Proyecto)
    frasePortafolio=models.CharField(max_length=200,verbose_name="Frase de presentación del portafolio",null=True)
    class Meta:
        verbose_name="Presentacion de la pagina principal del: Portafolio de proyectos"
        verbose_name_plural="Presentacion de la pagina principal del: Portafolio de proyectos"
 

 
'''
class Proyecto(models.Model):
    
    imagen=models.ImageField(verbose_name="Imagen del proyecto",upload_to="fotosProyectos")
    titulo=models.CharField(max_length=100,verbose_name="Titulo del proyecto")
    terminoProyecto=models.DateField(verbose_name="Fecha de creacion del proyecto: ",default=now,null=True)
    

    prioridad=models.PositiveSmallIntegerField(verbose_name="Prioridad de aparicion",default=0)
    preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)

    descripccion=models.TextField(verbose_name="Descripccion del proyecto:",default="")
    contenido=models.TextField(verbose_name="Descripccion mas extensa de lo que que trata el proyecto : ",default="",null=True)

    # 'auto_now_add' añadira la hora a la cual se creado el modelo
    #fechaCreacion=models.DateTimeField(auto_now_add=True)

    # 'auto_now' modificara la hora cada vez que se actualice la instancia
    #fechaModificacion=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"

        # del mas nuevo al mas antiguo usar '-'
        # del mas antigua a las nuevo NO USAR '-'
        ordering=['prioridad']

    def __str__(self):
        return "Proyecto: {}".format(self.titulo)

'''