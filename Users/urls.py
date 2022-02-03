from django.urls import path
from .views import TrainerList, TrainerDetail, NewCard

urlpatterns = [
    path("", TrainerList.as_view(), name="trainer_list"),
    path("<int:pk>/", TrainerDetail.as_view(), name="trainer_detail"),
    path("card/", NewCard.as_view(), name="new_card"),
]