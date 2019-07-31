# Generated by Django 2.2.3 on 2019-07-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_archivo', models.ImageField(upload_to='gallery')),
                ('nombre_imagen', models.CharField(max_length=200)),
                ('descripcion_imagen', models.TextField()),
            ],
        ),
    ]
