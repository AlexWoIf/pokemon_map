from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', )
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
                            related_name='next_evolutions',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True,
                            verbose_name='Происходит от', )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,
                                related_name='entities',
                                verbose_name='Покемон', )
    lat = models.FloatField(verbose_name='Широта', )
    lon = models.FloatField(verbose_name='Долгота', )
    appeared_at = models.DateTimeField(verbose_name='Время появления', )
    disappeared_at = models.DateTimeField(verbose_name='Время исчезновения', )
    level = models.IntegerField(verbose_name='Уровень',
                                null=True, blank=True, )
    health = models.IntegerField(verbose_name='Здоровье',
                                 null=True, blank=True, )
    strength = models.IntegerField(verbose_name='Сила',
                                   null=True, blank=True, )
    defence = models.IntegerField(verbose_name='Защита',
                                  null=True, blank=True, )
    stamina = models.IntegerField(verbose_name='Выносливость',
                                  null=True, blank=True, )

    def __str__(self):
        return self.pokemon.title
