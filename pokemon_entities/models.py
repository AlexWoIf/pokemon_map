from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    title = models.CharField(max_length=200, blank=True, )
    image = models.ImageField(upload_to='pokemons', null=True, blank=True)

    def __str__(self):
        return self.title
