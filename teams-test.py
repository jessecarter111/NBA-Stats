from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

year = 2020

#url page to be scraped
url = "https://www.basketball-reference.com/teams/"

html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")

soup.findAll('tr', limit=2)

headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]

# avoid the first header row
rows = soup.findAll('tr')[1:]

team_stats = [[td.getText() for td in rows[i].findAll(['th', 'td'])] for i in range(0, len(rows))]

for x in team_stats:
    if x[3] == '2019-20':
        print(x)

#stats = pd.DataFrame(team_stats, columns = headers)
#print(stats)
##for x in player_stats:
##        for y in x:
##            print(y)
#        break

#print(player_stats[1])
#for x in player_stats:
#    for i, y in enumerate(headers):
#        print(x[i])
#    break