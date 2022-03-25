from django.urls import path
from . import views


app_name="portafolio_app"

urlpatterns = [
    path('portafolio/inicio/',views.PortafolioEmpresa.as_view(),name='portafolio-inicio'),
    path('portafolio/<pk>/proyecto/',views.ProyectoDetailView.as_view(),name='portafolio-articuloDetail'),   

    # API...

    # CRUD DSE PROYECTOS...
    path('api/proyecto/list/',views.ProyetoListApiView.as_view(),name="proyecto_list_api"),
    path('api/proyecto/update/<pk>/',views.ProyectoUpdateApiView.as_view(),name="proyecto_update_api"),
    path('api/proyecto/create',views.ProyectoCreateApiView.as_view(),name="proyecto_create_api"),
    path('api/proyecto/delete/<pk>/',views.ProyectoDeleteApiView.as_view(),name="proyecto_delete_api"),
    path('api/proyecto/detail/<pk>/',views.ProyectoDetailApiView.as_view(),name='proyecto_detail_api'),


    
    # CATEGORIAS..
    path('api/categoria/list/',views.CategoriaListApiView.as_view(),name="categoria_list_api"),
    path('api/categoria/update/<pk>/',views.CategoriaUpdateApiView.as_view(),name="categoria_update_api"),
    path('api/categoria/create',views.CategoriaCreateApiView.as_view(),name="categoria_create_api"),

    # REACCIONES...
    path('api/proyecto/like/<pk>/',views.DarLike_ApiView.as_view(),name="proyecto_like_api"),
    path('api/proyecto/dislike/<pk>/',views.DarDislike_ApiView.as_view(),name="proyecto_like_api"),
    path('api/proyecto/visita/<pk>/',views.VisitarProyecto_ApiView.as_view(),name="proyecto_like_api"),

]