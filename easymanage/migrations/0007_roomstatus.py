# Generated by Django 2.0.5 on 2019-11-05 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easymanage', '0006_auto_20191105_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(max_length=4)),
                ('room_type', models.CharField(choices=[('Food', 'Food'), ('Beverages', 'Beverages'), ('Food&Beverages', 'Beverages'), ('MaintenanceCost', 'MaintenanceCost')], default=None, max_length=10)),
                ('room_description', models.TextField()),
                ('room_status', models.BooleanField(default=True)),
                ('customer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roomstatus', to='easymanage.Customer')),
            ],
        ),
    ]