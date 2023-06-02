# Generated by Django 4.2.1 on 2023-06-02 22:17

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo')),
                ('cedula', models.CharField(max_length=255, unique=True, verbose_name='Cédula de Identidad')),
                ('telefono', models.CharField(max_length=255, unique=True, verbose_name='Teléfono')),
                ('calificacion', models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=0, verbose_name='Calificación')),
                ('direccion', models.TextField(blank=True, null=True, verbose_name='Dirección')),
                ('foto_perfil', models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='Foto de perfil')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('terminos_y_condiciones', models.BooleanField(default=False, verbose_name='Términos y condiciones')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', authentication.models.UsuarioManager()),
            ],
        ),
    ]
