from rest_framework import  serializers
from .models import Categoria, Proyecto


class Proyecto_info_Serializer(serializers.ModelSerializer):
    '''
    Retornara la informacion basica de un proyecto...
    '''

    interpretacionCalif=serializers.SerializerMethodField()
    class Meta:
        model=Proyecto
        #fields='__all__'
        #     
        fields=(
            'id',
            'titulo',
            'descripccion',
            'contenido',
            'likes',
            'visitas',
            'calificacionCliente',
            'interpretacionCalif'
        )
    
    def get_interpretacionCalif(self,obj):
        return Proyecto.SATISFACCION_CLIENTE[obj.calificacionCliente]


class Proyecto_crearEditar_Serializer(serializers.ModelSerializer):
    '''
    Retornara la informacion basica de un proyecto...
    '''

    
    class Meta:
        model=Proyecto
        #fields='__all__'
        #     
        fields=(
            'preparadoParaMostrar',
            'titulo',
            'descripccion',
            'contenido',
            'calificacionCliente',
            'prioridad',     
        )



class Proyecto_eliminar_Serializer(serializers.ModelSerializer):
    '''
    Retornara la informacion basica de un proyecto...
    '''

    class Meta:
        model=Proyecto
        fields='__all__'


class Categoria_info_Serializer(serializers.ModelSerializer):
    '''
    Retornara la informacion basica de un proyecto...
    '''

    class Meta:
        model=Categoria
        fields=(
        'id',
        'nombre',
        )


class Categoria_editarCrearEliminar_Serializer(serializers.ModelSerializer):
    '''
    Retornara la informacion basica de un proyecto...
    '''

    class Meta:
        model=Categoria
        fields='__all__'


