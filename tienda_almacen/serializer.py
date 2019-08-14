from rest_framework import serializers
from tienda_almacen.models import Producto
from tienda_almacen.models import Categoria



class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'id_categoria', 'nombre_categoria')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url','id_producto','nombre_producto','cantidad_producto','precio_unidad','descripcion','images', 'categoria_id')

    

