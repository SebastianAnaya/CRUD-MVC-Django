# Generated by Django 4.1.1 on 2022-09-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('documento', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('usuario', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('id_tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.tipo_documento')),
                ('lugar_de_residencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.ciudad')),
            ],
        ),
    ]
