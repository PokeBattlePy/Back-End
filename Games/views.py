from rest_framework.views import APIView
from rest_framework.response import Response

from GameLogic.damage_calculator import attack
from GameLogic.create_pokemon import create_pokemon
from GameLogic.handle_attack import calculations

from .models import Game
from Users.models import Trainer
from .serializer import GameSerializer

from rest_framework.permissions import IsAuthenticated, AllowAny
import random

def filter_user_games(request):
    return Game.objects.filter(id=int(request.data['game']))
    
    
class Create_Join_Game(APIView):
    permission_classes = (AllowAny)
    
    def post(self, request):
        user_deck = request.data["deck"]
        rando = random.choice(Trainer.objects.all())
        ghost = rando.name
        computer_deck = create_pokemon(rando.decks)
        new_game = Game(owner = request.user, 
                            user_pokemon = user_deck,
                            comp_pokemon = computer_deck, 
                            active_user_pokemon = user_deck[0],
                            active_comp_pokemon = computer_deck[0],
                            ghost = ghost,
                            user_poke_status = user_deck,
                            comp_poke_status = computer_deck
                            )
        new_game.save()
        #return Response(GameSerializer(new_game).data)
        response = Response(GameSerializer(new_game).data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        
    


class GameDetail(APIView):
    permission_classes = (AllowAny)
    
    
    def put(self, request):
        comp_selections = ['base', 'special', 'defense']
        queryset = filter_user_games(request)
        game = GameSerializer(queryset[0]).data
        user_selection = request.data['selection']
        
        calculations(game, 'user','comp', user_selection)
        
        comp_selection = random.choices(comp_selections, weights=(40,50,10))[0]
        if comp_selection != 'defense':
            last_move = game['active_comp_pokemon']['moves'][comp_selection]['name']
            print(last_move)
        else:
            last_move = "defense"
        calculations(game, 'comp', 'user', comp_selection)
        
        
        queryset.update(last_move= last_move)
   
        
        queryset.update(active_comp_pokemon= game['active_comp_pokemon'])
        queryset.update(active_user_pokemon = game['active_user_pokemon'])
        queryset.update(user_pokemon = game['user_pokemon'])
        queryset.update(comp_pokemon = game['comp_pokemon'])
        
        #return Response(GameSerializer(queryset[0]).data)
        response = Response(GameSerializer(queryset[0]).data)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
        

                

        
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
        if len(pokemon_list) > 0:
            game[f'active_{targeted_user}_pokemon'] = pokemon_list.pop(0)
        else:
            # No More Pokemon :(
            return
    else:
        target['stats']['hp'] == updated_target['stats']['hp']

        
        
        
        
        
        
        
        
        
        
    # queryset = filter_user_games(request)
    #     # game = GameSerializer(queryset[len(queryset) - 1]).data
    #     game = GameSerializer(queryset[0]).data

    #     # If the user selects defense, give their pokemon a flat stat buff
    #     if request.data['selection'] == 'defense':
    #         game['active_user_pokemon']['stats']['defense'] = game['active_player_pokemon']['stats']['defense'] + 10
    #         game['active_player_pokemon']['stats']['special-defense'] = game['active_player_pokemon']['stats']['special-defense'] + 10
    #     else:
    #         move = game['active_player_pokemon']['moves'][request.data["selection"]]
            
            
    #         attacker = game['active_player_pokemon']
    #         target = game['active_comp_pokemon']
    #         updated_target = attack(attacker,target,move)
    #         if updated_target['stats']['hp'] <= 0:
    #             game['comp_pokemon'].pop(0)
    #             if game['comp_pokemon']:
    #                 game['active_comp_pokemon'] = game['comp_pokemon'][0]
    #             else:
    #                 #User has won!
    #                 pass
        
        