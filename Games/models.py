from django.db import models
from django.contrib.auth import get_user_model

class Game(models.Model):
    ghost = models.CharField(max_length=16, default="Computer")
    user_pokemon = models.JSONField(default=list)
    comp_pokemon = models.JSONField(default=list)
    user_poke_status = models.JSONField(default=list)
    comp_poke_status = models.JSONField(default=list)
    active_user_pokemon = models.JSONField(default=dict)
    active_comp_pokemon = models.JSONField(default=dict)
    last_move = models.CharField(max_length=16, default="smack")