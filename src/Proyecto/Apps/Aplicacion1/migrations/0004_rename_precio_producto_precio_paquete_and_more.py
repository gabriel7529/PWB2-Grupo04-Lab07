# Generated by Django 4.1 on 2022-08-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0003_rename_products_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='precio_paquete',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_unidad',
            field=models.DecimalField(decimal_places=2, default=25.0, max_digits=4),
            preserve_default=False,
        ),
    ]