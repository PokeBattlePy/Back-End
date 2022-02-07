import random
import pokebase

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

    if not attack.power:
        attack.power = 55
    if not special.power:
        special.power = 55
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

if __name__ == '__main__':
    print(init_cards())