# Generated by Django 4.2.1 on 2023-06-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0012_roomplan_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomplan',
            name='ppm',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
