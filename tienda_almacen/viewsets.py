from rest_framework import viewsets
from .models import Producto
from .models import Categoria

from .serializer import ProductoSerializer
from .serializer import CategoriaSerializer



class CategoriaViewSets(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()   
    serializer_class = CategoriaSerializer

class ProductoViewSets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    
    '''queryset2 = Producto.objects.filter(id_producto=5)
    queryset2.delete()'''
    serializer_class = ProductoSerializer


class ListaProductos2(viewsets.ModelViewSet):
    queryset = Producto.objects.all()[4:]
    serializer_class = ProductoSerializer

  