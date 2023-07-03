# Generated by Django 4.2.1 on 2023-06-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_rename_kind_plan_plan_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='room_type',
            new_name='madori',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='plan_type',
            new_name='plan',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='name',
        ),
        migrations.AddField(
            model_name='plan',
            name='alcove',
            field=models.CharField(blank=True, help_text='2.50m²', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='balcony',
            field=models.CharField(blank=True, help_text='2.50m²', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='measurement',
            field=models.CharField(blank=True, help_text='6.0m×6.0m', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='menu',
            field=models.CharField(blank=True, help_text='基本...', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='terrace',
            field=models.CharField(blank=True, help_text='2.50m²', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='type',
            field=models.CharField(blank=True, help_text='A, B', max_length=255, null=True),
        ),
    ]
