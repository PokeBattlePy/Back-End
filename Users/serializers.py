from rest_framework import serializers
from .models import Trainer, PokemonCard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCard
        fields = "__all__"