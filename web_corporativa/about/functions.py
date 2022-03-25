
from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib import admin


class ApartadoManager(models.Manager):

    def get_apartado(self):
        '''
        Retornara el apartado cuya fecha de creación sea la mas reciente,
        siempre y cuando este disponible para ser mostrada
        '''

        return self.filter(preparadoParaMostrar=True).order_by('-created').first()


class Apartado(TimeStampedModel):
    # Lo que hara  'upload_to' es guardar las imagenes en una carpeta con el nombre
    # del valor que se asigne a 'upload_to' 
    # ¿y si no existe la carpeta? R=Se creara la carpeta
    # ¿y donde estara ubicada dicha carpeta? 
    # R= Dentro del directorio media que fue indicado en el archivo 'settings.py' de 
    # Django a traves de las costantes: 'MEDIA_URL' y 'MEDIA_ROOT' 
    preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)
    nombre=models.CharField(verbose_name="Nombre del diseño de portada:", max_length=150,null=True)
    imagenPortada=models.ImageField(verbose_name="Imagen del apartado de portada:",upload_to="fotosApartados")

    objects=ApartadoManager()

    def __str__(self):
        return "Apartado con codigo: {}".format(self.id)





class ApartadoAdmin(admin.ModelAdmin):
    list_display=('nombre','created','modified','preparadoParaMostrar')
    readonly_fields=(
        'created',
        'modified'
    )

    # ordenando del mas reciente al menos reciente
    ordering=('-created',)


#class Apartado(TimeStampedModel):
    # Lo que hara  'upload_to' es guardar las imagenes en una carpeta con el nombre
    # del valor que se asigne a 'upload_to' 
    # ¿y si no existe la carpeta? R=Se creara la carpeta
    # ¿y donde estara ubicada dicha carpeta? 
    # R= Dentro del directorio media que fue indicado en el archivo 'settings.py' de 
    # Django a traves de las costantes: 'MEDIA_URL' y 'MEDIA_ROOT' 
 #   imagenPortada=models.ImageField(verbose_name="Imagen del apartado de portada:",upload_to="fotosApartados")
 #   preparadoParaMostrar=models.BooleanField(verbose_name="¿La publicación esta lista para ser mostrada? ",default=False)

 #   def __str__(self):
 #       return "Apartado con codigo: {}".format(self.id)