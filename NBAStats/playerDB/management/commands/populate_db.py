from django.core.management.base import BaseCommand, CommandError
from ... models import Player, Team
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'
    
    def populate_players(self):
        data = self.scrape_players()
        #the headers of the data are the column names
        headers = data[0]
        #the players data is their stats indexed in the same order as the headers
        player_data = data[1]
        fields = Player._meta.fields

        #cleaning data so fields are not null
        for p in player_data:
            for i, x in enumerate(p):
                if p[i] == '':
                    p[i] = '0'
        print(len(player_data[0]))
        for p in player_data:
            if len(p) == 29:
                if not Player.objects.filter(player_name=p[0]).exists() and Team.objects.filter(team_abrev=p[3]):
                    entry = Player(player_name=p[0], position=p[1], age=p[2], team=Team.objects.get(team_abrev=p[3]), games=p[4],\
                                games_started=p[5], minutes_played=p[6], field_goals=p[7],\
                                field_goals_attempted=p[8], field_goals_pct=p[9], three_pts=p[10],\
                                three_pts_attempted=p[11], three_pts_pct=p[12], two_pts=p[13],\
                                two_pts_attempted=p[14], two_pts_pct=p[15], effective_fg_pct=p[16],\
                                points=p[17], free_throws=p[18], free_throws_attempted=p[19],\
                                free_throws_pct=p[20], off_reb=p[21], def_reb=p[22], total_reb=p[23],\
                                assists=p[24], steals=p[25], blocks=p[26], turnovers=p[27], pers_fouls=p[28])
                    entry.save()

        self.stdout.write(self.style.SUCCESS('Updated/Populated Players'))

    def populate_teams(self):
        team_codes = {'Atlanta Hawks':'ATL', 'Boston Celtics':'BOS', 'Brooklyn Nets':'BRK', 
                        'Charlotte Hornets':'CHO', 'Chicago Bulls':'CHI','Cleveland Cavaliers':'CLE',
                        'Dallas Mavericks':'DAL', 'Denver Nuggets':'DEN', 'Detroit Pistons':'DET',
                        'Golden State Warriors':'GSW', 'Houston Rockets':'HOU', 'Indiana Pacers':'IND',
                        'LA Clippers':'LAC', 'LA Lakers':'LAL', 'Memphis Grizzlies':'MEM',
                        'Miami Heat':'MIA', 'Milwaukee Bucks':'MIL', 'Minnesota Timberwolves':'MIN',
                        'New Orleans Pelicans':'NOP', 'New York Knicks':'NYK', 'Oklahoma City Thunder':'OKC',
                        'Orlando Magic':'ORL', 'Philadelphia Sixers':'PHI', 'Phoenix Suns':'PHX', 
                        'Portland Trail Blazers':'POR', 'Sacramento Kings':'SAC', 'San Antonio Spurs':'SAS',
                        'Toronto Raptors':'TOR', 'Utah Jazz':'UTA', 'Washington Wizards':'WAS'}

        data = self.scrape_teams()
        headers = data[0]
        team_stats = data[1]

        for team in team_stats:
            #check that there isn't already a team with the same name entered to prevent duplicates
            if not Team.objects.filter(team_name=team[0]).exists():
                if team_codes.get(team[0]):
                    team_entry = Team(team_name=team[0], team_abrev=team_codes[team[0]], league=team[1],
                    inaug=team[2], end=team[3], years=team[4], games=team[5], wins=team[6], losses=team[7],
                    w_l_pct=team[8], playoffs=team[9], division=team[10], conference=team[11], championships=team[12])
                    print(team_entry)
                    team_entry.save()
        
        self.stdout.write(self.style.SUCCESS('Updated/Populated Teams'))
    
        
    def handle(self, *args, **options):
        #pulls all individual players stats from the 2020 season from bball-reference
        self.populate_teams()
        self.populate_players()
        

    def scrape_players(self):
        #url page to be scraped
        url = "https://www.basketball-reference.com/leagues/NBA_2020_per_game.html"

        html = urlopen(url)

        soup = BeautifulSoup(html, features="html.parser")

        soup.findAll('tr', limit=2)

        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        headers = headers [1:]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]
        player_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

        return [headers, player_stats]

    def scrape_teams(self):
        #url page to be scraped
        url = "https://www.basketball-reference.com/teams/"

        html = urlopen(url)

        soup = BeautifulSoup(html, features="html.parser")

        soup.findAll('tr', limit=2)

        headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

        # avoid the first header row
        rows = soup.findAll('tr')[1:]

        team_stats = [[td.getText() for td in rows[i].findAll(['th', 'td'])] for i in range(0, len(rows))]

        return [headers, team_stats]