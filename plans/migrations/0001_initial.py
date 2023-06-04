# Generated by Django 4.2.1 on 2023-06-04 09:27

from django.db import migrations, models
import plans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('kind', models.CharField(blank=True, choices=[('general_plan', '一般図'), ('room_plan', '間取り図')], default='general_plan', max_length=255)),
                ('name', models.CharField(blank=True, help_text='A, B or 敷地配置図', max_length=255)),
                ('image', models.FileField(upload_to=plans.models.upload_to)),
                ('room_type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['order_num'],
            },
        ),
    ]
