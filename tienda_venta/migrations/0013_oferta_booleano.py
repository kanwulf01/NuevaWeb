# Generated by Django 2.2.3 on 2019-07-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_venta', '0012_auto_20190730_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='booleano',
            field=models.BooleanField(default=False),
        ),
    ]