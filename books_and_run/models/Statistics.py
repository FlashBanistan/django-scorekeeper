from django.db import models
from django.contrib.auth.models import User

class Statistics(models.Model):
    # Define model fields:
    user = models.OneToOneField(User, primary_key=True)
    games_won = models.IntegerField(null=True, blank=True)
    hands_won = models.IntegerField(null=True, blank=True)
    games_played = models.IntegerField(null=True, blank=True)
    high_score = models.IntegerField(null=True, blank=True)
    low_score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    def increment_games_won(self):
        self.games_won = self.games_won + 1
        return self.games_won

    def increment_hands_won(self, number_hands_won):
        self.hands_won = self.hands_won + number_hands_won
        return self.hands_won

    def increment_games_played(self):
        self.games_played = self.games_played + 1
        return self.games_played

    def edit_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score

    def edit_low_score(self, score):
        if score < self.low_score:
            self.low_score = score
        return self.low_score

    class Meta:
        verbose_name_plural = "statistics"
