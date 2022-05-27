from django.db import models
from django.urls import reverse



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
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    logo = models.ImageField(upload_to='manufacturers/logos/')
    date_created = models.DateField()
    code = models.CharField(max_length=100)
    founder = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    activities = models.CharField(max_length=100)
    summary = models.TextField()
    history = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('fabriquant', kwargs={"slug": self.slug})
