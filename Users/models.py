from django.contrib.auth import get_user_model
from django.db import models
import pokebase
import random
import json

rarities = ["common", "uncommon", "rare", "epic", "legendary"]
multiplier = {"common":1, "uncommon":1.1, "rare":1.2, "epic":1.3, "legendary":1.4}


def create_card(rarity=None, pokemon_int=None):
    if not pokemon_int:
      pokemon_int = random.randint(1, 151)
    pokemon_obj = pokebase.pokemon(pokemon_int)
    name = pokemon_obj.name
    if not rarity:
      rarity = random.choices(rarities, weights=(50, 30, 14, 5, 1))[0]
    types = []
    for type in pokemon_obj.types:
      types.append(type.type.name)
    moves = [pokemon_obj.moves[1].move.name, pokemon_obj.moves[0].move.name]
    official_artwork = getattr(pokemon_obj.sprites.other, "official-artwork").front_default
    front = pokemon_obj.sprites.front_default
    back = pokemon_obj.sprites.back_default
    base_stats = pokemon_obj.stats

    # stats = {"hp":{"stat": base_stats[0].base_stat, "type": }, 
    # "attack":{"stat": base_stats[1].base_stat, "type": }, 
    # "defense":{"stat": base_stats[2].base_stat, "type": },
    # "special-attack":{"stat": base_stats[3].base_stat, "type": }}

    obj = {"pokemon_int":pokemon_int, 
    "name":name, 
    "rarity":rarity, 
    "types":types, 
    "moves":moves, 
    "official_artwork":official_artwork, 
    "front":front, 
    "back":back, 
    # "stats":stats
    }
    print(str(obj))
    return obj

class Trainer(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=32)
    decks = models.JSONField(default=list)
    cards = models.JSONField(default=[create_card(), create_card()])
    prev_battles = models.JSONField(default=list)



