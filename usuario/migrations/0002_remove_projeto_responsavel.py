# Generated by Django 3.0.7 on 2020-06-29 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='responsavel',
        ),
    ]