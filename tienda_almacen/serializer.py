from rest_framework import serializers
from tienda_almacen.models import Producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('url','id_producto','nombre_producto','cantidad_producto','precio_unidad','descripcion','images')

    

