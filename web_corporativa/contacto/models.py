from django.db import models
from about.functions import Apartado

# Create your models here.
class Apartado_Contacto(Apartado):
    pass

    class Meta:
        verbose_name="Presentacion de la pagina de: contacto"

class MensajeRecibido(models.Model):
    asunto=models.CharField(verbose_name="Asunto del mensaje",max_length=300)
    mensaje=models.TextField(verbose_name="Cuerpo del mensaje")

    class Meta:
        verbose_name="Mensaje de confirmacion de recibido"
        verbose_name_plural="Mensaje de confirmacion de recibido"
    
    def __str__(self):
        return "formato de mensaje con id:{}".format(self.id)


class RedCotacto(models.Model):
    # REDES SOCIALES
    FACEBOOK_RED_SOCIAL='1'
    YOUTUBE_RED_SOCIAL='2'
    INSTAGRAM_RED_SOCIAL='3'
    LINKEDIN_RED_SOCIAL='4'
    TWITTER_RED_SOCIAL='5'
    GITHUB_RED_SOCIAL='6'

    REDES_SOCIALES={
        FACEBOOK_RED_SOCIAL:"Facebook",
        YOUTUBE_RED_SOCIAL:"Youtube",
        INSTAGRAM_RED_SOCIAL:"Instragram",
        LINKEDIN_RED_SOCIAL:"LinkedIn",
        TWITTER_RED_SOCIAL:"Twitter",
        GITHUB_RED_SOCIAL:"Github"
    }

    nombreRedContacto=models.CharField(
        verbose_name="Red social",
        max_length=1,
        choices=tuple(REDES_SOCIALES.items()),
        unique=True
    )

    url=models.URLField(verbose_name="Enlace",max_length=200,null=True,blank=True)
    
    class Meta:
        verbose_name="Red de contacto"
        verbose_name_plural="Redes de contacto"
        ordering=['nombreRedContacto']
    
    def __str__(self):
        return "{}".format( self.REDES_SOCIALES[self.nombreRedContacto]  )