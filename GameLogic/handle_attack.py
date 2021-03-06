from GameLogic.damage_calculator import attack

def calculations(game, attacking_user, targeted_user, selection):
    target = game[f'active_{targeted_user}_pokemon']
    attacker = game[f'active_{attacking_user}_pokemon']
    pokemon_list = game[f'{targeted_user}_pokemon']

    if selection == 'defense':
        attacker['stats']['defense'] = attacker['stats']['defense'] + 10
        attacker['stats']['special-defense'] = attacker['stats']['special-defense'] + 10
        return
        
    move = attacker['moves'][selection]
    updated_target = attack(attacker,target,move)
    if updated_target['stats']['hp'] <= 0:
        if len(pokemon_list) > 1:
            pokemon_list.pop(0)
            game[f'active_{targeted_user}_pokemon'] = pokemon_list[0]
        else:
            # No More Pokemon :(
            game[f'active_{targeted_user}_pokemon'] = None
    else:
        target['stats']['hp'] == updated_target['stats']['hp']