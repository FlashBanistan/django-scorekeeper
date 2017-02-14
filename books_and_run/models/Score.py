from django.db import models
from django.contrib.auth.models import User
from books_and_run.models import Game

class Score(models.Model):
    # Define model fields:
    player = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    created_on = models.DateTimeField(auto_now_add=True)
    round_one = models.IntegerField(null=True, blank=True)
    round_two = models.IntegerField(null=True, blank=True)
    round_three = models.IntegerField(null=True, blank=True)
    round_four = models.IntegerField(null=True, blank=True)
    round_five = models.IntegerField(null=True, blank=True)
    round_six = models.IntegerField(null=True, blank=True)
    round_seven = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    def get_total(self):
        return self.round_one + self.round_two + self.round_three + self.round_four + self.round_five + self.round_six + self.round_seven

    def get_best_round(self):
        pass

    def get_worst_round(self):
        pass

    def get_average(self):
        return self.get_total() / self.game.rounds
