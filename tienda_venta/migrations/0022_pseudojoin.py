# Generated by Django 2.2.3 on 2019-08-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0008_auto_20190729_2231'),
        ('tienda_venta', '0021_auto_20190801_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='PseudoJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedidos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Pedido')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_almacen.Producto')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda_venta.Cliente2')),
            ],
        ),
    ]