from django.db import models

# Create your models here.


class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    cantidad_producto = models.IntegerField()
    precio_unidad = models.BigIntegerField()
    photo = models.URLField(max_length=500, blank=True, default='')
    descripcion = models.CharField(max_length=200, default="")
    images = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.nombre_producto



class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    producto = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE)

    class meta:
        unique_together = ('course', 'nombre_categoria')


class imagen(models.Model):
    url_imagen = models.CharField(max_length=100,default='')
    productox = models.ForeignKey(Producto, blank=True, on_delete=models.CASCADE, default=0)
    class meta:
        unique_together = ('url_imagen','productox')