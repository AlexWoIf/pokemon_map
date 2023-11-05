from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    title = models.CharField(max_length=200, blank=True, )
    title_en = models.CharField(max_length=200, blank=True, )
    title_jp = models.CharField(max_length=200, blank=True, )
    description = models.TextField(blank=True, )
    image = models.ImageField(upload_to='pokemons', null=True, blank=True, )
    previous_evolution = models.ForeignKey(
                            'self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True, )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=1)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)

    def __str__(self):
        return self.pokemon.title
