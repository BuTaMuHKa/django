# Generated by Django 3.0 on 2020-06-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0020_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bboard.Rubric', verbose_name='Рубрика'),
        ),
    ]