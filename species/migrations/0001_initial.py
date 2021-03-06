# Generated by Django 4.0 on 2022-05-27 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='species', verbose_name='Image')),
                ('governance', models.TextField(blank=True, null=True, verbose_name='Gouvernance')),
                ('sovereignty', models.TextField(blank=True, null=True, verbose_name='Souverainet√©')),
                ('philosophy', models.TextField(blank=True, null=True, verbose_name='Philosophie')),
                ('religion', models.TextField(blank=True, null=True, verbose_name='Religion')),
                ('origin', models.TextField(blank=True, null=True, verbose_name='Origine')),
                ('first_contact', models.TextField(blank=True, null=True, verbose_name='1er contact')),
            ],
        ),
    ]
