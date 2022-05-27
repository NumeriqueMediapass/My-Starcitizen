# Generated by Django 4.0 on 2022-05-27 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0002_species_slug'),
        ('ship', '0007_alter_ship_cargo_capacity_alter_ship_crew_capacity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='specie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='species.species', verbose_name='Espèce'),
            preserve_default=False,
        ),
    ]