from django.db import models
from django.urls import reverse

"""
Espèces
- Nom
- Slug
- Description
- Image
- Gouvernance
- Souveraineté
- Philosophie
- Religion
- Origine
- 1er contact
"""


class Species(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    image = models.ImageField(upload_to='species', blank=True, null=True, verbose_name="Image")
    governance = models.TextField(verbose_name="Gouvernance", null=True, blank=True)
    sovereignty = models.TextField(verbose_name="Souveraineté", null=True, blank=True)
    philosophy = models.TextField(verbose_name="Philosophie", null=True, blank=True)
    religion = models.TextField(verbose_name="Religion", null=True, blank=True)
    origin = models.TextField(verbose_name="Origine", null=True, blank=True)
    first_contact = models.TextField(verbose_name="1er contact", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('espece', kwargs={"slug": self.slug})
