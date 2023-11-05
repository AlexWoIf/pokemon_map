from django.db import models


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    title = models.CharField(max_length=200, blank=True,
                             verbose_name='Название', )
    title_en = models.CharField(max_length=200, blank=True,
                                verbose_name='Название (англ.)', )
    title_jp = models.CharField(max_length=200, blank=True,
                                verbose_name='Название (яп.)', )
    description = models.TextField(blank=True,
                                   verbose_name='Описание', )
    image = models.ImageField(upload_to='pokemons', null=True, blank=True,
                              verbose_name='Изображение', )
    previous_evolution = models.ForeignKey(
                            'self',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            verbose_name='Происходит от', )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта', )
    lon = models.FloatField(verbose_name='Долгота', )
    appeared_at = models.DateTimeField(verbose_name='Время появления', )
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', )
    level = models.IntegerField(default=1, verbose_name='Уровень', )
    health = models.IntegerField(default=1, verbose_name='Здоровье', )
    strength = models.IntegerField(default=1, verbose_name='Сила', )
    defence = models.IntegerField(default=1, verbose_name='Защита', )
    stamina = models.IntegerField(default=1, verbose_name='Выносливость', )

    def __str__(self):
        return self.pokemon.title
