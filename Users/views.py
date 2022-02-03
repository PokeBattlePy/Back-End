from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Trainer, create_card
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response


class TrainerList(ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Trainer.objects.all()
    serializer_class = UserSerializer


class TrainerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Trainer.objects.all()
    serializer_class = UserSerializer
        
    
class NewCard(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        trainer = Trainer.objects.filter(owner=request.user.id)
        trainer.update(cards=[create_card()]+trainer[0].cards)
        return Response(UserSerializer(trainer[0]).data)