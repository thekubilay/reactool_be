# Generated by Django 4.2.1 on 2023-06-02 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_alter_gallery_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='url',
            new_name='file',
        ),
    ]
