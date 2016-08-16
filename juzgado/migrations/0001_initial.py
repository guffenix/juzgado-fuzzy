# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afectado',
            fields=[
                ('id_afectado', models.AutoField(serialize=False, primary_key=True)),
                ('cedula_afectado', models.CharField(max_length=10)),
                ('telf_afectado', models.CharField(max_length=16)),
                ('nombre_afectado', models.CharField(max_length=32)),
                ('apellido_afectado', models.CharField(max_length=32)),
                ('direccion_afectado', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Delincuente',
            fields=[
                ('id_delincuente', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_delincuente', models.CharField(max_length=32)),
                ('apellido_delincuente', models.CharField(max_length=32)),
                ('sexo_delincuente', models.CharField(max_length=10)),
                ('edad_delincuente', models.IntegerField()),
                ('piel_delincuente', models.CharField(max_length=16)),
                ('estatura_delincuente', models.FloatField()),
                ('contextura_delincuente', models.CharField(max_length=32)),
                ('cabello_delincuente', models.CharField(max_length=32)),
                ('color_cabello_delincuente', models.CharField(max_length=32)),
                ('color_ojos_delincuente', models.CharField(max_length=32)),
                ('nariz_delincuente', models.CharField(max_length=32)),
                ('forma_rostro_delincuente', models.CharField(max_length=32)),
                ('senial_delincuente', models.CharField(max_length=32)),
                ('bello_facial_delincuente', models.CharField(max_length=32)),
                ('foto_delincuente', models.ImageField(upload_to='img_delincuente/')),
            ],
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id_denuncia', models.AutoField(serialize=False, primary_key=True)),
                ('movil_denuncia', models.CharField(max_length=16)),
                ('lugar_denuncia', models.CharField(max_length=32)),
                ('fecha_denuncia', models.DateField()),
                ('hora_denuncia', models.TimeField()),
                ('direccion_denuncia', models.TextField()),
                ('id_afectado', models.ForeignKey(to='juzgado.Afectado')),
            ],
        ),
        migrations.CreateModel(
            name='Sospecha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('id_delincuente', models.ForeignKey(to='juzgado.Delincuente')),
            ],
        ),
        migrations.CreateModel(
            name='Sospechoso',
            fields=[
                ('id_sospechoso', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_sospechoso', models.CharField(max_length=32)),
                ('apellido_sospechoso', models.CharField(max_length=32)),
                ('sexo_sospechoso', models.CharField(max_length=10)),
                ('edad_sospechoso', models.IntegerField()),
                ('piel_sospechoso', models.CharField(max_length=16)),
                ('estatura_sospechoso', models.FloatField()),
                ('contextura_sospechoso', models.CharField(max_length=32)),
                ('cabello_sospechoso', models.CharField(max_length=32)),
                ('color_cabello_sospechoso', models.CharField(max_length=32)),
                ('color_ojos_sospechoso', models.CharField(max_length=32)),
                ('nariz_sospechoso', models.CharField(max_length=32)),
                ('forma_rostro_sospechoso', models.CharField(max_length=32)),
                ('senial_sospechoso', models.CharField(max_length=32)),
                ('bello_facial_sospechoso', models.CharField(max_length=32)),
                ('bosquejo_sospechoso', models.ImageField(upload_to='img_sospechoso/')),
                ('id_denuncia', models.ForeignKey(to='juzgado.Denuncia')),
            ],
        ),
        migrations.AddField(
            model_name='sospecha',
            name='id_sospechoso',
            field=models.ForeignKey(to='juzgado.Sospechoso'),
        ),
        migrations.AlterUniqueTogether(
            name='sospecha',
            unique_together=set([('id_sospechoso', 'id_delincuente')]),
        ),
    ]
