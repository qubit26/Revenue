# Generated by Django 4.2.1 on 2023-06-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_mensaje_visto_notificacion_visto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Valor'),
        ),
    ]
