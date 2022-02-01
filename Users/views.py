from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Trainer, PokemonCard
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, CardSerializer


class TrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = UserSerializer


class TrainerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Trainer.objects.all()
    serializer_class = UserSerializer


class CardList(ListCreateAPIView):
    queryset = PokemonCard.objects.all()
    serializer_class = CardSerializer

class CardDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = PokemonCard.objects.all()
    serializer_class = CardSerializer