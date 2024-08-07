# Generated by Django 4.2.14 on 2024-07-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_deparment_employees_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='phone',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='salary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
