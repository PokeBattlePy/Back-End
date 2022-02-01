from type_table import type_table

def get_type_modifier(atk_type,def_types):
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