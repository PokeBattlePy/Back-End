from django.contrib.auth import get_user_model
from django.db import models
import pokebase
import random


rarities = ["common", "uncommon", "rare", "epic", "legendary"]
multiplier = {"common":0.25, "uncommon":0.5, "rare":0.75, "epic":0.80, "legendary":1}

class PokemonCard(models.Model):
    
    pokemon_int = random.randint(1, 151)
    

    pokemon_obj = pokebase.pokemon(pokemon_int)

        
        
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=32, default=pokemon_obj.name)
    rarity = models.CharField(max_length=32, default=random.choices(rarities, weights=(50, 30, 14, 5, 1))[0])
    types = pokemon_obj.types
    moves = models.JSONField(default=[pokemon_obj.moves[1].move.name, pokemon_obj.moves[0].move.name])


class Trainer(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=32)
    decks = models.JSONField(default=list)
    cards = models.ForeignKey(PokemonCard, on_delete=models.CASCADE)
    prev_battles = models.JSONField(default=list)



