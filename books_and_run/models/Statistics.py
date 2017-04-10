from django.db import models
from django.contrib.auth.models import User

class Statistics(models.Model):
    # Define model fields:
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    games_won = models.IntegerField(default=0)
    hands_won = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    high_score = models.IntegerField(null=True, blank=True)
    low_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    def increment_games_won(self, is_winner):
        if is_winner is True:
            self.games_won = self.games_won + 1
        return self.games_won

    def add_to_hands_won(self, num_hands_won):
        if num_hands_won > 0 and num_hands_won < 8:
            self.hands_won = self.hands_won + num_hands_won
        return self.hands_won

    # Need to somehow add a check to validate if the user was actually in the game.
    def increment_games_played(self):
        self.games_played = self.games_played + 1
        return self.games_played

    def new_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

    def new_low_score(self, score):
        if score < self.low_score:
            self.low_score = score
        return self.low_score

    class Meta:
        verbose_name_plural = "statistics"
