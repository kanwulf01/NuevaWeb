from rest_framework import viewsets

from .serializer import Cliente2Serializer, LoginSerializer, OfertaSerializer, JoinFalso, JoinFalso2

from .serializer import Cliente2Serializer, LoginSerializer, OfertaSerializer, getProductsSerializer

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente2,PseudoJoin

from .models import OfertaProducto

from .models import Oferta




class ClienteViewSets(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    serializer_class = Cliente2Serializer

class ClienteLogin(viewsets.ModelViewSet):
    
    queryset = Cliente2.objects.all()
    serializer_class = LoginSerializer



class OfertaViewSets(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()
    serializer_class = OfertaSerializer


'''Join entre Modelo cliente oferta y Productos'''
class ProductosIDS(viewsets.ModelViewSet):
    queryset = OfertaProducto.objects.all()
    serializer_class = OfertaSerializer


class viewjoin(viewsets.ModelViewSet):

    queryset = PseudoJoin.objects.all()
    serializer_class = JoinFalso



class VistaPrueba(viewsets.ModelViewSet):
    queryset = PseudoJoin.objects.all()
    serializer_class = JoinFalso2