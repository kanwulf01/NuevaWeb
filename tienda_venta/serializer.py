from rest_framework import serializers
from .models import Cliente2
from .models import OfertaProducto, PseudoJoin
from tienda_almacen.models import Producto
from tienda_almacen.serializer import ProductoSerializer



from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente2
        fields = ('cedula','nombre','url','lastname','email','phone','seller','contra')





class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'

   


class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PseudoJoin
        fields = '__all__'


class JoinFalso(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PseudoJoin
        fields = ('id','url','vendedor','productos')

class JoinFalso2(serializers.ModelSerializer):
    vendedor = LoginSerializer()
    productos = ProductoSerializer()
    class Meta:
        model = PseudoJoin
        fields = ('id','url','vendedor','productos')
