# Generated by Django 3.0.7 on 2020-06-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_auto_20200630_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='projeto/'),
        ),
    ]
