from damage_calculator import calc_damage
from damage_calculator import attack
from damage_calculator import get_type_modifier
def test_super_effective():
    attack_type = 'water'
    target_types = ['fire']
    expected = 2
    actual = get_type_modifier(attack_type,target_types)
    assert actual == expected

def test_double_super_effective():
    attack_type = 'fire'
    target_types = ['grass','steel']
    expected = 4
    actual = get_type_modifier(attack_type,target_types)
    assert actual == expected

def test_not_very_effective():
    attack_type = 'fire'
    target_types = ['water']
    expected = 0.5
    actual = get_type_modifier(attack_type,target_types)
    assert actual == expected

def test_double_ineffective():
    attack_type = 'fire'
    target_types = ['water','rock']
    expected = 0.25
    actual = get_type_modifier(attack_type,target_types)
    assert actual == expected

def test_immune():
    attack_type = 'poison'
    target_types = ['steel']
    expected = 0
    actual = get_type_modifier(attack_type,target_types)
    assert actual == expected

def test_damage_calc():
    attacker = {"pokemon_int": 37, "name": "vulpix", "rarity": "epic", "types": ["fire"], "moves": {"base": {"name": "body-slam", "power": 85, "class": "physical", "type": "normal"}, "special": {"name": "headbutt", "power": 70, "class": "physical", "type": "normal"}}, "official_artwork": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/37.png", "front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/37.png", "back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/37.png", "stats": {"hp": 28.4, "attack": 53.300000000000004, "special-attack": 65.0, "defense": 62.0, "special-defense": 94.5}}
    defender = {"pokemon_int": 44, "name": "gloom", "rarity": "common", "types": ["grass", "poison"], "moves": {"base": {"name": "cut", "power": 50, "class": "physical", "type": "normal"}, "special": {"name": "swords-dance", "power": 0, "class": "status", "type": "normal"}}, "official_artwork": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/44.png", "front": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/44.png", "back": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/44.png", "stats": {"hp": 60, "attack": 65, "special-attack": 85, "defense": 70, "special-defense": 75}}
    move = attacker['moves']['base']
    assert calc_damage(attacker,defender,move)
