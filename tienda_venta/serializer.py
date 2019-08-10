from rest_framework import serializers
from .models import Cliente2

from .models import OfertaProducto, PseudoJoin
from tienda_almacen.models import Producto
from tienda_almacen.serializer import ProductoSerializer

from .models import OfertaProducto
from tienda_almacen.models import Producto




from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente2
        fields = ('cedula','nombre','url','lastname','email','phone','seller','contra')





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
        model = OfertaProducto
        fields = '__all__'

