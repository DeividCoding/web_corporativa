from django.urls import path
from . import views


app_name="dashboard_app"

# dashboard_app:dashboard-inicio
urlpatterns=[
    path('dashboard/inicio/',views.DashBoard_Inicio.as_view(),name="dashboard-inicio"),
]