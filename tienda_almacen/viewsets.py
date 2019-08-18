from rest_framework import viewsets,filters, generics
import django_filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Producto
from .models import Categoria

from .serializer import ProductoSerializer
from .serializer import CategoriaSerializer

class ContactFilter(django_filters.FilterSet):
   class Meta:
        model = Producto
        fields = {
            'categoria_id': ['startswith']
        }
        together = ['categoria_id']


class PCategoriaViewSets(viewsets.ModelViewSet):   
    serializer_class = ProductoSerializer
    def get_queryset(self):
    	selectd = self.request.GET.get('q')
    	return Producto.objects.filter(categoria_id__startswith=selectd)


    
    


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

  