# Generated by Django 4.2.1 on 2023-06-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='imagenes',
            field=models.ManyToManyField(blank=True, to='management.imagenesoferta', verbose_name='Imagenes de la Oferta'),
        ),
    ]
