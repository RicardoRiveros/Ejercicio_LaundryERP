from django.urls import path
from . import views
app_name='usuarios'

urlpatterns = [
    path('', views.index, name='usuarios/usuarios.html')
]
