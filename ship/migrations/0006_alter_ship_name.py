# Generated by Django 4.0 on 2022-05-27 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0005_alter_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]