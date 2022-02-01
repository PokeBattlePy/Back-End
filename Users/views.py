from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Trainer
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer


class TrainerList(ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = UserSerializer


class TrainerDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Trainer.objects.all()
    serializer_class = UserSerializer


