# Generated by Django 3.0.7 on 2020-06-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_projeto_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='arquivo',
            field=models.FileField(upload_to='projeto/'),
        ),
    ]