from django.db import models

# Create your models here.
"""
Vaisseaux
- Nom
- Constructeur
- Longueur
- Largeur
- Hauteur
- Masse à vide
- Capacité de chargement
- Equipage minimum
- Logo
"""


class Ship(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    empty_mass = models.FloatField()
    cargo_capacity = models.FloatField()
    crew_capacity = models.IntegerField()
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    def __str__(self):
        return self.name
