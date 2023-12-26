# Generated by Django 4.2.6 on 2023-12-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('idBanner', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(blank=True, db_column='title', max_length=255, null=True, verbose_name='Banner Title')),
                ('titulo', models.CharField(blank=True, db_column='titulo', max_length=255, null=True, verbose_name='Titulo en Español')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banners/')),
            ],
            options={
                'verbose_name_plural': '01 Banners',
                'db_table': 'Banners',
                'ordering': ['-date'],
            },
        ),
    ]
