# Generated by Django 4.2.1 on 2023-06-15 12:31

from django.db import migrations, models
import django.db.models.deletion
import plans.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_project_status'),
        ('plans', '0010_plan_thumbnail_alter_plan_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralPlan',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('image', models.ImageField(upload_to=plans.models.upload_to)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_plans', to='projects.project')),
            ],
            options={
                'ordering': ['order_num'],
            },
        ),
        migrations.CreateModel(
            name='RoomPlan',
            fields=[
                ('id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('order_num', models.IntegerField(default=1, null=True)),
                ('image', models.ImageField(upload_to=plans.models.upload_to)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=plans.models.upload_to)),
                ('type', models.CharField(blank=True, help_text='A, B, 立面図', max_length=255, null=True)),
                ('menu', models.CharField(blank=True, help_text='基本...', max_length=255, null=True)),
                ('madori', models.CharField(blank=True, help_text='2LDK, 4LDK+WIC', max_length=255, null=True)),
                ('measurement', models.CharField(blank=True, help_text='62.10m²', max_length=255, null=True)),
                ('alcove', models.CharField(blank=True, help_text='2.50m²', max_length=255, null=True)),
                ('terrace', models.CharField(blank=True, help_text='2.50m²', max_length=255, null=True)),
                ('balcony', models.CharField(blank=True, help_text='2.50m²', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_plans', to='projects.project')),
            ],
            options={
                'ordering': ['order_num'],
            },
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
