# Generated by Django 2.0.5 on 2019-11-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0002_auto_20191105_0155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_DOB',
            field=models.DateField(),
        ),
    ]