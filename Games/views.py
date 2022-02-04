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
    permission_classes = (AllowAny,)
    
    def post(self, request):
        print("Incoming Request")
        print(request)
        print("Request Data")
        print(request.data)
        user_deck = request.data['body']["deck"]
        rando = random.choice(Trainer.objects.all())
        ghost = rando.name
        computer_deck = create_pokemon(rando.decks)
        new_game = Game(user_pokemon = user_deck,
                        comp_pokemon = computer_deck, 
                        active_user_pokemon = user_deck[0],
                        active_comp_pokemon = computer_deck[0],
                        ghost = ghost,
                        user_poke_status = user_deck,
                        comp_poke_status = computer_deck
                        )

        return Response(GameSerializer(new_game).data)
        
    


class GameDetail(APIView):
    permission_classes = (AllowAny,)
    
    
    def put(self, request):
        print("Incoming Request")
        print(request)
        print("Request Data")
        print(request.data)
        comp_selections = ['base', 'special', 'defense']
        
        game = request.data["body"]["game"]
        user_selection = request.data['selection']
        
        calculations(game, 'user','comp', user_selection)
        
        comp_selection = random.choices(comp_selections, weights=(40,50,10))[0]
        if comp_selection != 'defense':
            last_move = game['active_comp_pokemon']['moves'][comp_selection]['name']
            print(last_move)
        else:
            last_move = "defense"
        calculations(game, 'comp', 'user', comp_selection)
        
        return Response(game)
        
        

        

        
        
        
        
        
        
        
        
        
        
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
        
        