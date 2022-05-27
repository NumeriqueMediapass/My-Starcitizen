from django.db import models
from django.urls import reverse
from species.models import Species

"""
Fabriquant :
- Nom
- Logo
- Date de création
- Code
- Fondateur
- Siege social
- Activité(s)
- Résumé
- Histoire
"""


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=100, verbose_name="Slug")
    logo = models.ImageField(upload_to='manufacturers/logos/', verbose_name="Logo")
    date_created = models.DateField(verbose_name="Date de création")
    code = models.CharField(max_length=100, verbose_name="Code")
    founder = models.CharField(max_length=100, verbose_name="Fondateur")
    headquarters = models.CharField(max_length=100, verbose_name="Siege social")
    activities = models.CharField(max_length=100, verbose_name="Activité(s)")
    summary = models.TextField(verbose_name="Résumé")
    history = models.TextField(verbose_name="Histoire")
    spacie = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="Espèce")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fabriquant', kwargs={"slug": self.slug})
