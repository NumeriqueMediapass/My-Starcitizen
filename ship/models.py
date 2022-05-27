from django.db import models
from manufacturer.models import Manufacturer
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


"""
Rôle
- Nom
- Description
"""


class Role(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


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
- Equipage maximum
- Logo
"""


class Ship(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=100)
    length = models.FloatField(verbose_name="Longueur")
    width = models.FloatField(verbose_name="Largeur")
    height = models.FloatField(verbose_name="Hauteur")
    empty_mass = models.FloatField(verbose_name="Masse à vide")
    cargo_capacity = models.FloatField(verbose_name="Capacité de chargement")
    crew_capacity = models.IntegerField(verbose_name="Equipage minimum")
    crew_capacity_max = models.IntegerField(verbose_name="Equipage maximum")
    logo = models.ImageField(upload_to='logos', blank=True, null=True, verbose_name="Image")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='manufacturer',
                                     verbose_name="Constructeur")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Statut")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Rôle")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vaisseau', kwargs={"slug": self.slug})
