# Generated by Django 4.0 on 2022-05-27 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0003_manufacturer_ship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='ship',
        ),
    ]