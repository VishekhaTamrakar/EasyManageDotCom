# Generated by Django 2.0.5 on 2019-11-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_stay_start_date',
            field=models.DateField(),
        ),
    ]