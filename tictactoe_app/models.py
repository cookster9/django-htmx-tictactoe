from django.db import models

# Create your models here.
class Game(models.Model):
    board_ary = models.CharField(max_length=200, default=" , , , , , , , , ")
    player_turn = models.IntegerField(default=1)
    winner = models.IntegerField(null=True, default=None)