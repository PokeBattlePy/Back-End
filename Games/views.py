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
        print("Playing Round")
        comp_selections = ['base', 'special', 'defense']
        
        game = request.data["body"]["game"]
        user_selection = request.data['body']['selection']
        
        calculations(game, 'user','comp', user_selection)
        
        comp_selection = random.choices(comp_selections, weights=(40,50,10))[0]
        
        if comp_selection != 'defense' and game['active_comp_pokemon'] is not None:
            game['last_move'] = game['active_comp_pokemon']['moves'][comp_selection]['name']
        else:
            game['last_move'] = "defense"
        #THIS IS THE PROBLEM!! LOSERS CANT ATTACK!!!
        #TODO: Fix This
        if game['active_comp_pokemon'] is not None:
            calculations(game, 'comp', 'user', comp_selection)
        
        return Response(game)
        
        


        