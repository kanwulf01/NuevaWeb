from rest_framework import serializers
from tienda_almacen.models import Producto
from tienda_almacen.models import Categoria



class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url','id_producto','nombre_producto','cantidad_producto','precio_unidad','descripcion','images', 'categoria_id')

    

