from django.db import models

# Create your models here.
class Player(models.Models):
    player_name = models.CharField(max_length=100)
    position = models.CharField(max_length=5)
    age = models.IntegerField()
    team = models.CharField(max_length=3)
    games = models.IntegerField()
    games_started = models.IntegerField()
    minutes_played = models.DecimalField(..., max_digits=3, decimal_places=1)
    field_goals = models.IntegerField()
    field_goals_attempted = models.IntegerField()
    field_goals_pct = models.DecimalField(..., max_digits=3, decimal_places=3)
    three_pts = models.IntegerField()
    three_pts_attempted = models.IntegerField()
    three_pts_pct = models.DecimalField(..., max_digits=3, decimal_places=3)
    two_pts = models.IntegerField()
    two_pts_attempted = models.IntegerField()
    two_pts_pct = models.DecimalField(..., max_digits=3, decimal_places=3)
    effective_fg_pct = models.DecimalField(..., max_digits=3, decimal_places=3)
    free_throws = models.DecimalField(..., max_digits=3, decimal_places=1)
    free_throws_attempted = models.DecimalField(..., max_digits=3, decimal_places=1)
    free_throws_pct = models.DecimalField(..., max_digits=3, decimal_places=3)



    minutes_played = models.DecimalField(..., max_digits=3, decimal_places=1)