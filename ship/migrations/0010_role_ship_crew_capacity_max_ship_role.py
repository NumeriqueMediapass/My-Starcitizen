# Generated by Django 4.0 on 2022-05-27 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0009_remove_ship_specie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ship',
            name='crew_capacity_max',
            field=models.IntegerField(default=1, verbose_name='Equipage maximum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ship',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ship.role', verbose_name='Rôle'),
            preserve_default=False,
        ),
    ]
