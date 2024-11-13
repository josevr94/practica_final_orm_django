from django.urls import path
from . import views

urlpatterns = [
    path('lista/',views.lista_laboratorio,name='lista'),
    path('',views.agregar,name='formulario'),
    path('editar/<int:pk>/',views.actualizar,name='editar'),
    path('eliminar/<int:pk>/',views.eliminar,name='eliminar'),
]
