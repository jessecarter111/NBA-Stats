from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length = 100)
    wins = models.IntegerField()
    losses = models.IntegerField()


class PlayerManager(models.Manager):
    def create_player(self, player_name):
        player = self.create(player_name = player_name)
        return player

class Player(models.Model):
    #Meta
    player_name = models.CharField(max_length=100)
    position = models.CharField(max_length=5)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    #Gametime
    games = models.IntegerField()
    games_started = models.IntegerField()
    minutes_played = models.DecimalField(max_digits=3, decimal_places=1)
    #Scoring
    field_goals = models.IntegerField()
    field_goals_attempted = models.IntegerField()
    field_goals_pct = models.DecimalField(max_digits=3, decimal_places=3)
    three_pts = models.IntegerField()
    three_pts_attempted = models.IntegerField()
    three_pts_pct = models.DecimalField(max_digits=3, decimal_places=3)
    two_pts = models.IntegerField()
    two_pts_attempted = models.IntegerField()
    two_pts_pct = models.DecimalField(max_digits=3, decimal_places=3)
    effective_fg_pct = models.DecimalField(max_digits=3, decimal_places=3)
    points = models.DecimalField(max_digits=3, decimal_places=1)
    #Free Throws
    free_throws = models.DecimalField(max_digits=3, decimal_places=1)
    free_throws_attempted = models.DecimalField(max_digits=3, decimal_places=1)
    free_throws_pct = models.DecimalField(max_digits=3, decimal_places=3)
    #Boards
    off_reb = models.DecimalField(max_digits=3, decimal_places=1)
    def_reb = models.DecimalField(max_digits=3, decimal_places=1)
    total_reb = models.DecimalField(max_digits=3, decimal_places=1)
    #Assist
    assists = models.DecimalField(max_digits=3, decimal_places=1)
    #Steals
    steals = models.DecimalField(max_digits=3, decimal_places=1)
    #Blocks
    blocks = models.DecimalField(max_digits=3, decimal_places=1)
    #Turnovers
    turnovers = models.DecimalField(max_digits=3, decimal_places=1)
    #Personal Fouls
    pers_fouls = models.DecimalField(max_digits=3, decimal_places=1)