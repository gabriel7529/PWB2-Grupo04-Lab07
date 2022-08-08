# Generated by Django 4.1 on 2022-08-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fecha_carga', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
