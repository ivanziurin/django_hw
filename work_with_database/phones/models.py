from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.FileField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50)
