# Generated by Django 3.0.7 on 2020-06-30 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_projeto_aprovado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='aprovado',
            new_name='status',
        ),
    ]
