from .type_table import type_table

def get_type_modifier(atk_type:str,def_types:list) -> int:
  def_type_one = def_types[0].lower()
  def_type_two = None

  if len(def_types) == 2:
    def_type_two = def_types[1].lower()

  result = 1.0
  if atk_type in type_table[def_type_one]['weaknesses']:
    result *= 2
  elif atk_type in type_table[def_type_one]['resistances']:
    result *= .5
  elif atk_type in type_table[def_type_one]['immunities']:
    result *= 0
  if def_type_two:
    if atk_type in type_table[def_type_two]['weaknesses']:
      result *= 2
    elif atk_type in type_table[def_type_two]['resistances']:
      result *= .5
    elif atk_type in type_table[def_type_two]['immunities']:
      result *= 0
  return result

def is_STAB(poke:dict,move:dict) -> bool:
  return move['type'] in poke['types']

def calc_damage(atk_poke:dict,def_poke:dict,move:dict) -> int:
  """
  inputs: Attacking Pokemon Object, Definding Pokemon Object, Move Object
  output: Int
  """
  #Constant for pokemon level, adjust this for tweaking final damage output
  LEVEL = 10

  atk = None
  defense = None

  # Determine whether to use special or physical stats will result in type int
  if move['class'] == 'special':
    atk = atk_poke['stats']['special-attack']
    defense = def_poke['stats']['special-defense']
  else:
    atk = atk_poke['stats']['attack']
    defense = def_poke['stats']['defense']

  # Determines weakness / resistance modifier based on defending pokemon's typings
  type_modifier = get_type_modifier(move['type'], def_poke['types'])

  # Determines modifier based on pokemon stats
  level_modifier = (2 * LEVEL / 5 + 2)
  atk_def_ratio = (atk / defense)
  head_to_head_modifier = (level_modifier *atk_def_ratio / 50)

  # Determines damage before accounting for types
  adjusted_damage = head_to_head_modifier * move['power'] + 2
 
  # Multipies damage by 1.5 if move type matches attacking pokemon's type
  STAB = is_STAB(atk_poke,move)
  STAB_modifier = 1
  if STAB:
    STAB_modifier = 1.5

  # Final Damage Caculation
  final_dmg = adjusted_damage * STAB_modifier * type_modifier

  # Return Rounded Damage Value
  return int(final_dmg)

def update_health(poke:dict,damage:int) -> None:
  poke['stats']['hp'] = poke['stats']['hp'] - damage

def attack(atk_poke:dict,def_poke:dict,move:dict) -> None:
  """
  could be made into a method on the attacking pokemon
  """

  damage_dealt = calc_damage(atk_poke,def_poke,move)
  update_health(def_poke,damage_dealt)
  return def_poke