from django.urls import path
from . import views
from .views import home, contacto, galeria, productos, carrito, limpiar_carrito, checkout, ProductoViewSet
from rest_framework import routers
from django.urls import include, path
from app import views

router = routers.DefaultRouter()
router.register(r'productoss', ProductoViewSet)


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('productos/', productos, name="productos"),
    path('carrito/', carrito, name="carrito"),
    path('agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('limpiar-carrito/', limpiar_carrito, name='limpiar_carrito'),
    path('checkout/', checkout, name='checkout'),

    path('', include(router.urls)),

]
