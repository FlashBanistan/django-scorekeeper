from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    # Define model fields:
    players = models.ManyToManyField(User)
    max_players = models.IntegerField(default=8, editable=False)
    rounds = models.IntegerField(default=7, editable=False)
    winner = models.ForeignKey(User, null=True, blank=True, related_name='game_winner')
    created_on = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(User)  // Possibly add this if needed.

    def __str__(self):
        return str(self.pk)
