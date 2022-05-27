# Generated by Django 4.0 on 2022-05-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='manufacturers/logos/')),
                ('date_created', models.DateField()),
                ('code', models.CharField(max_length=100)),
                ('founder', models.CharField(max_length=100)),
                ('headquarters', models.CharField(max_length=100)),
                ('activities', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('history', models.TextField()),
            ],
        ),
    ]