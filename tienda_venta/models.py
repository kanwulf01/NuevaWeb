from django.db import models
from tienda_suscripcion.models import Tienda
from tienda_almacen.models import Producto

# Create your models here.


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=30,default="")
    nombre = models.CharField(max_length=20, default="")
    lastname = models.CharField(max_length=20, default="")
    direccion = models.CharField(max_length=20, default="")
    creditcard = models.IntegerField(default=0)
    passw = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=20, default="")
    seller = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, default="")
  

class Cliente2(models.Model):
    cedula = models.CharField(primary_key=True, max_length=30)
    nombre = models.CharField(max_length=20, default="")
    lastname = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=30, default="")
    phone = models.CharField(max_length=20, default="")
    seller = models.BooleanField(default=False)
    contra = models.CharField(max_length=20,default="")

    '''def retorna(self):
        queryset = Cliente2.objects.filter(contra=self.contra)
        return 'funciono'''


   

class Pedido(models.Model):
    numero_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, blank=True, on_delete=models.CASCADE)
''' clases Oferta y Compra nuevos, que describen? existe una relacion articulo,tienda(vendedor) oferta'''
''' Esta relacion me permite que para cada oferta en la tienda se tenga una clase compra que se asigna a oferta'''
'''Esta compra la realiza un CLiente y a su vez la clase compra gerenra una factura y un envio'''



class Factura(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    date = models.DateField()
    precioTotal = models.BigIntegerField()
    nombre_cliente = models.CharField(max_length=20)
    comprax = models.CharField(max_length=20)


class Envio(models.Model):
    id_envio = models.IntegerField(primary_key=True)
    dir_destino = models.CharField(max_length=30)
    precio_envio = models.IntegerField()
    date = models.DateField()
    hora = models.DateTimeField()
    factura = models.ForeignKey(Factura, blank=True, on_delete=models.CASCADE)

class Venta(models.Model):
    tienday = models.ForeignKey(Tienda, blank=True, on_delete=models.CASCADE)
    productoy = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, blank=True, on_delete=models.CASCADE, default=0)


        
'''MODELADO DE PRUEBA '''
'''
class ClienteOferta(models.Model):
    tienday = models.ForeignKey(Cliente2, blank=True, on_delete=models.CASCADE)
    productoy = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)
    ofertx = models.AutoField(primary_key=True, default=False)
'''

class Compra(models.Model):
    numero_compra = models.CharField(max_length=30)
    oferta = models.CharField(max_length = 30)



class OfertaProducto(models.Model):
    tiendaz = models.ForeignKey(Cliente2, blank=True, on_delete=models.CASCADE)
    productoz = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)
    ofertaz = models.AutoField(primary_key=True)
   

class Oferta(models.Model):
    booleano = models.BooleanField(default=False)
    ofertaz = models.ForeignKey(OfertaProducto, blank=True, on_delete=models.CASCADE)
