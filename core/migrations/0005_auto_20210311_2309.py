# Generated by Django 3.1.7 on 2021-03-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210311_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='description',
            field=models.TextField(max_length=300, verbose_name='Descrição'),
        ),
    ]
