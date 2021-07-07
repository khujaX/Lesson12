from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="sites/")
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name
