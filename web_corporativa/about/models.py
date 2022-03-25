from django.db import models
from about.functions import Apartado

# Create your models here.

class Apartado_About(Apartado):
    foto=models.ImageField(verbose_name="Foto de la empresa:",upload_to="fotosEmpresa")    
    descripccion=models.TextField(verbose_name="Descripccion de empresa:",default="")

    class Meta:
        verbose_name="Presentacion de la pagina de: about"
        verbose_name_plural="Presentacion de la pagina de: about"

class DatosEmpresa(models.Model):
    nombre=models.CharField(max_length=150,verbose_name="Nombre:")
    sector=models.CharField(max_length=150,verbose_name="Sector:")
    fechaNacimiento=models.DateField(verbose_name="Fecha de creacion:")

    correoElectronico=models.EmailField(verbose_name="Correo electronico: ",null=True,default=None)
    numeroTelefonico=models.CharField(max_length=50,null=True,default=None)

    class Meta:
        verbose_name="Datos de la empresa"
        verbose_name_plural="Datos de la empresa"

    def __str__(self):
        return "{}-{}".format(self.id,self.nombre)


