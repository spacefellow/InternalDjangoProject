# Generated by Django 3.2.5 on 2021-07-28 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockinfo',
            name='slug',
            field=models.SlugField(verbose_name='URL'),
        ),
    ]
