from django.urls import path
from .views import Create_Join_Game, GameDetail


urlpatterns = [
    path("", Create_Join_Game.as_view(), name="create_join_game"),
    path('battle/',GameDetail.as_view(), name='game_detail')
]