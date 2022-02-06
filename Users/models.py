from django.contrib.auth import get_user_model
from django.db import models
import pokebase
import random
import json

rarities = ["common", "uncommon", "rare", "epic", "legendary"]
multipliers = {"common":1, "uncommon":1.1, "rare":1.2, "epic":1.3, "legendary":1.4}


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
    
    official_artwork = getattr(pokemon_obj.sprites.other, "official-artwork").front_default
    front = pokemon_obj.sprites.front_default
    back = pokemon_obj.sprites.back_default
    base_stats = pokemon_obj.stats
    multiplier = multipliers[rarity]
    attack = pokebase.move(pokemon_obj.moves[1].move.name)
    special = pokebase.move(pokemon_obj.moves[0].move.name)

    moves = {
    "base":{"name":pokemon_obj.moves[1].move.name, "power": attack.power|55, "class":attack.damage_class.name, "type": attack.type.name}, 
    "special": {"name":pokemon_obj.moves[0].move.name, "power": special.power|55, "class":special.damage_class.name, "type": special.type.name}
    }
    
    stats = {
    "hp": base_stats[0].base_stat*multiplier, 
    "attack": base_stats[1].base_stat*multiplier, 
    "special-attack": base_stats[3].base_stat*multiplier,
    "defense": base_stats[2].base_stat*multiplier,
    "special-defense": base_stats[4].base_stat*multiplier
    }

    obj = {"pokemon_int":pokemon_int, 
    "name":name, 
    "rarity":rarity, 
    "types":types, 
    "moves":moves, 
    "official_artwork":official_artwork, 
    "front":front, 
    "back":back, 
    "stats":stats,}
    return obj

def init_cards():
  return [create_card(), create_card()]

class Trainer(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True
    )
    name = models.CharField(max_length=32)
    decks = models.JSONField(default=list)
    cards = models.JSONField(default=[{'pokemon_int': 150, 'name': 'mewtwo', 'rarity': 'uncommon', 'types': ['psychic'], 'moves': {'base': {'name': 'pay-day', 'power': 63, 'class': 'physical', 'type': 'normal'}, 'special': {'name': 'mega-punch', 'power': 119, 'class': 'physical', 'type': 'normal'}}, 'official_artwork': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png', 'front': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png', 'back': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/150.png', 'stats': {'hp': 116.60000000000001, 'attack': 121.00000000000001, 'special-attack': 169.4, 'defense': 99.00000000000001, 'special-defense': 99.00000000000001}}, {'pokemon_int': 25, 'name': 'pikachu', 'rarity': 'uncommon', 'types': ['electric'], 'moves': {'base': {'name': 'pay-day', 'power': 63, 'class': 'physical', 'type': 'normal'}, 'special': {'name': 'mega-punch', 'power': 119, 'class': 'physical', 'type': 'normal'}}, 'official_artwork': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png', 'front': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png', 'back': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/25.png', 'stats': {'hp': 38.5, 'attack': 60.50000000000001, 'special-attack': 55.00000000000001, 'defense': 44.0, 'special-defense': 55.00000000000001}}])
    prev_battles = models.JSONField(default=list)




