from django.contrib import admin
from .models import Game, Score, Statistics

admin.site.register([Game, Score, Statistics])
