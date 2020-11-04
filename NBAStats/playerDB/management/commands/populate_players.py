from django.core.management.base import BaseCommand, CommandError
from ... models import Player, Team, PlayerManager
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'Scrapes bball-ref for players stats, adds them to the db if they aren\'t already in there'

    def handle(self, *args, **options):
        #pulls all individual players stats from the 2020 season from bball-reference
        data = self.scrape_players()
        #the headers of the data are the column names
        headers = data[0]
        #the players data is their stats indexed in the same order as the headers
        player_data = data[1]
        fields = Player._meta.fields
        for p in player_data:
            entry = Player(player_name=p[0], position=p[1], age=p[2], team=p[3], games=p[4],\
                           games_started=p[5], minutes_played=p[6], field_goals=p[7],\
                           field_goals_attempted=p[8], field_goals_pct=p[9], three_pts=p[10],\
                           three_pts_attempted=p[11], three_pts_pct=[12], two_pts=p[13],\
                           two_pts_attempted=p[14], two_pts_pct=[15], effective_fg_pct=p[16],\
                           points=p[17], free_throws=p[18], free_throws_attempted=p[19],\
                           free_throws_pct=p[20], off_reb=[21], def_reb=[22], total_reb=[23],\
                           assists=p[24], steals=p[25], blocks=p[26], turnovers=p[27], pers_fouls=p[28])
            print(entry)
            break
        #for player in player_data:
        #    entry = PlayerManager.create_player(player[0])
        #    for i in range(1, len(headers)):
        #        entry = PlayerManager.create_player(player[0])
        #        entry.fields[i] = player[i]
        #        entry.save()
        #    break
        self.stdout.write(self.style.SUCCESS('Printed fields'))

    def scrape_players(self):
        year = 2020

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
