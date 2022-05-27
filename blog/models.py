from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
