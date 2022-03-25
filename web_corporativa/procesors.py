from about.models import DatosEmpresa
from contacto.models import RedCotacto

def datos_autor(request):
    datosAutor=DatosEmpresa.objects.last()

    datosRetornar={
        'NOMBRE':"EMPRESA ANONIMA",
        'SECTOR':"SECTOR ANONIMO",
        'CORREO':None,
        'NUMERO_TELEFONO':None,
    }
    if datosAutor:
        datosRetornar['NOMBRE']=datosAutor.nombre
        datosRetornar['SECTOR']=datosAutor.sector
        datosRetornar['CORREO']=datosAutor.correoElectronico
        datosRetornar['NUMERO_TELEFONO']=datosAutor.numeroTelefonico   
        
    return datosRetornar


def contexto_contactos(request):
    redesSociales=dict( ("CONTACTO_"+str(redSocial),redSocial.url) for redSocial in RedCotacto.objects.all() )
    return redesSociales



