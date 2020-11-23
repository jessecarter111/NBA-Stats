# NBA-Stats
Django project to scrape, store, query and display stats for the NBA

To populate the DB usign webscraping run "python3 manage.py populate_db" which executes 2 scripts to populate the teams and players tables by pulling data from https://www.basketball-reference.com/
These scripts can be found in NBA-Stats/NBAStats/playerDB/management/commands/populate_db.py

Otherwise the project can be operated as normal. To access the admin page the username is "admin" and the password is "admin123".
