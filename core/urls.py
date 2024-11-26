from django.urls import path
from .views import Iniciar
from .views import Datos
from .views import Carrito
from .views import Reseta
from .views import editar_medic, eliminar_medic

urlpatterns = [
    path('',Iniciar, name='Iniciar'),
    path('Datos.html/',Datos,name='Datos'),
    path('Carrito.html/',Carrito,name='Carrito'),
    path('Reseta/',Reseta,name='Reseta'),
    path('editar-medic/<id>/',editar_medic,name='editar_medic'),
    path('eliminar-medic/<id>/',eliminar_medic,name='eliminar_medic'),

] 