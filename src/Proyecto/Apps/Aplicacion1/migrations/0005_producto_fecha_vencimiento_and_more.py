# Generated by Django 4.1 on 2022-08-08 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0004_rename_precio_producto_precio_paquete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fecha_vencimiento',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_paquete',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_unidad',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
