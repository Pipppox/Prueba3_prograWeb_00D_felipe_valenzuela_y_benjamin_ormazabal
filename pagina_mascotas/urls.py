from django.urls import path
from .views import index, adopta, crear_dieta, info_animales, lista_productos, ver_carrito, contactanos, login, registro, agregar_al_carrito, eliminar_del_carrito

urlpatterns = [
    path('', index, name='index'),
    path('adopta/', adopta, name='adopta'),
    path('crear_dieta/', crear_dieta, name='crear_dieta'),
    path('info_animales/', info_animales, name='info_animales'),
    path('productos/', lista_productos, name='lista_productos'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('contactanos/', contactanos, name='contactanos'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]