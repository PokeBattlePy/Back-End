from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

# class PokemonSerializer(serializers.Serializer):
#     pokemon_int = serializers.IntegerField()
#     name = serializers.CharField()
#     rarity = serializers.CharField()
#     types = serializers.ListField()
#     moves = serializers.DictField()
#     official_artwork = serializers.CharField()
#     front = serializers.CharField()
#     back = serializers.CharField()
#     stats = serializers.DictField()




