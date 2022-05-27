from django.db import models
from manufacturer.models import Manufacturer
from django.urls import reverse

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


class Status(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Ship(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    empty_mass = models.FloatField()
    cargo_capacity = models.FloatField()
    crew_capacity = models.IntegerField()
    logo = models.ImageField(upload_to='logos', blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    list_display = ['name', 'length', 'width', 'height', 'empty_mass', 'cargo_capacity', 'crew_capacity', 'manufacturer', 'status']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vaisseau', kwargs={"slug": self.slug})
