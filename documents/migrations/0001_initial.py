# Generated by Django 4.2.1 on 2023-07-09 04:34

from django.db import migrations, models
import django.db.models.deletion
import documents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('thumbnail', models.ImageField(blank=True, upload_to=documents.models.upload_to)),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('size', models.IntegerField(default=1, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='projects.project')),
            ],
            options={
                'ordering': ['order_num'],
            },
        ),
    ]
