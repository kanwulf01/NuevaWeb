from rest_framework import serializers
from .models import Cliente2
from .models import OfertaProducto
from tienda_almacen.models import Producto



from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'

    


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'


       


class getProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
   


class OfertaSerializer(serializers.ModelSerializer):
    producto = getProductsSerializer(read_only=True)
    class Meta:
        model = OfertaProducto
        fields = '__all__'