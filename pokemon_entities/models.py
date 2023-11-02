from django.db import models  # noqa F401

# your models here
class Pokemons(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    title = models.CharField(max_length=200, blank=True, )