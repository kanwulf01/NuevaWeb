from rest_framework import serializers
from .models import Cliente2


from rest_framework.fields import CurrentUserDefault

class Cliente2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'

    


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente2
        fields = '__all__'


       

