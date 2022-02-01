from django.urls import path
from .views import TrainerList, TrainerDetail

urlpatterns = [
    path("", TrainerList.as_view(), name="trainer_list"),
    path("<int:pk>/", TrainerDetail.as_view(), name="trainer_detail"),
]