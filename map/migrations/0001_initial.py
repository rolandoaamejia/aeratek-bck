# Generated by Django 4.2.6 on 2023-12-12 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('idMap', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now=True)),
                ('title', models.CharField(blank=True, db_column='title', max_length=255, null=True, verbose_name='Map Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='map/')),
            ],
            options={
                'verbose_name_plural': '01 Map',
                'db_table': 'Maps',
                'ordering': ['-date'],
            },
        ),
    ]
