# Generated by Django 4.0 on 2022-05-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('empty_mass', models.FloatField()),
                ('cargo_capacity', models.FloatField()),
                ('crew_capacity', models.IntegerField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
            ],
        ),
    ]
