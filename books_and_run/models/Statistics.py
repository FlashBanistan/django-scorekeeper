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

    class Meta:
        verbose_name_plural = "statistics"
