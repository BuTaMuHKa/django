# Generated by Django 3.0 on 2020-05-12 13:50

import bboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0017_auto_20200512_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd',
            name='photo',
            field=models.ImageField(upload_to=bboard.models.get_timestamp_path, verbose_name='фото'),
        ),
    ]