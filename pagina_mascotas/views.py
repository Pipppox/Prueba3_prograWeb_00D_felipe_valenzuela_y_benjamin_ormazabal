from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, CarritoItem

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'pagina_mascotas/productos.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_id = request.session.get('carrito_id')
    if not carrito_id:
        carrito = Carrito.objects.create()
        request.session['carrito_id'] = carrito.id
    else:
        carrito = Carrito.objects.get(id=carrito_id)
    
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    return redirect('ver_carrito')

def ver_carrito(request):
    carrito_id = request.session.get('carrito_id')
    if not carrito_id:
        carrito = None
        items = []
        total = 0
    else:
        carrito = get_object_or_404(Carrito, id=carrito_id)
        items = CarritoItem.objects.filter(carrito=carrito)
        total = carrito.total

    return render(request, 'pagina_mascotas/carrito.html', {'carrito': carrito, 'items': items, 'total': total})

def eliminar_del_carrito(request, producto_id):
    carrito_id = request.session.get('carrito_id')
    carrito = get_object_or_404(Carrito, id=carrito_id)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_item = get_object_or_404(CarritoItem, carrito=carrito, producto=producto)
    carrito_item.delete()
    
    return redirect('ver_carrito')

def index(request):
    return render(request, 'pagina_mascotas/index.html')

def adopta(request):
    return render(request, 'pagina_mascotas/adopta.html')

def crear_dieta(request):
    return render(request, 'pagina_mascotas/crear_dieta.html')

def info_animales(request):
    return render(request, 'pagina_mascotas/info_animales.html')

def contactanos(request):
    return render(request, 'pagina_mascotas/contactanos.html')

def login(request):
    return render(request, 'pagina_mascotas/login.html')

def registro(request):
    return render(request, 'pagina_mascotas/registro.html')