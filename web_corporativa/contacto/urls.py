from django.urls import path
from . import views


app_name="contacto_app"

urlpatterns=[
    #path('contact/',views.Contacto.as_view(),name="contact"),
    path('contact/',views.FormularioContacto.as_view(),name="contact"),
    path('exitoMensaje/',views.MensajeExito.as_view(),name="mensajeContactoExito")
]