# Generated by Django 4.0 on 2022-05-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0004_status_ship_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]