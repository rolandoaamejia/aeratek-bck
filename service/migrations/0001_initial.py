# Generated by Django 4.2.6 on 2023-12-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageService',
            fields=[
                ('idImageServices', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='imageServices/')),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '02 Images Services',
                'db_table': 'ImageService',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('idServices', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(blank=True, db_column='title', max_length=255, null=True, verbose_name='Service Title')),
                ('titulo', models.CharField(blank=True, db_column='titulo', max_length=255, null=True, verbose_name='Titulo del Servicio')),
                ('body', models.TextField(db_column='body', verbose_name='Service Body')),
                ('cuerpo', models.TextField(db_column='cuerpo', verbose_name='Cuerpo del Servicio en Español')),
                ('coverImage', models.ImageField(upload_to='coverServicesImage/')),
                ('Images', models.ManyToManyField(blank=True, to='service.imageservice')),
            ],
            options={
                'verbose_name_plural': '01 Services',
                'db_table': 'Services',
                'ordering': ['-date'],
            },
        ),
    ]
