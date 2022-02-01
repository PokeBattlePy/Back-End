from django.urls import path
from .views import TrainerList, TrainerDetail, CardList, CardDetail

urlpatterns = [
    path("trainer/", TrainerList.as_view(), name="trainer_list"),
    path("trainer/<int:pk>/", TrainerDetail.as_view(), name="trainer_detail"),
    path("card/", CardList.as_view(), name="card_list"),
    path("card/<int:pk>/", CardDetail.as_view(), name="card_detail"),
]