# Generated by Django 4.2.1 on 2023-06-24 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0002_alter_oferta_imagenes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(choices=[('TE HAN ENVIADO UN MENSAJE', 'TE HAN ENVIADO UN MENSAJE'), ('TU OFERTA HA SIDO COMPRADA', 'TU OFERTA HA SIDO COMPRADA')], max_length=75, verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('oferta', models.ForeignKey(blank='False', null='False', on_delete=django.db.models.deletion.CASCADE, to='management.oferta', verbose_name='Oferta')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Receptor')),
            ],
            options={
                'verbose_name': 'Notificacion',
                'verbose_name_plural': 'Notificaciones',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emisor_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Emisor')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Receptor')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'ordering': ['-fecha'],
            },
        ),
    ]
