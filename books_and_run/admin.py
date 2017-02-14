from django.contrib import admin
from .models import Game, Score

admin.site.register([Game, Score])
