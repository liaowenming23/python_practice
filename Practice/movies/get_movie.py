import requests
import pandas as pd
from bs4 import BeautifulSoup


url = 'https://movies.yahoo.com.tw/chart.html'

resp = requests.get(url)
resp.encoding = 'utf-8'

soup = BeautifulSoup(resp.text, 'lxml')

rows = soup.find_all('div', class_='tr')
colname = list(rows.pop(0).stripped_strings)

contents = []
for row in rows:
    thisweek_rank = row.find_next('div', attrs={'class': 'td'})
    updown = thisweek_rank.find_next('div')
    lastweek_rank = updown.find_next('div')

    if thisweek_rank.string == str(1):
        movie_title = lastweek_rank.find_next('h2')
    else:
        movie_title = lastweek_rank.find_next('div', attrs={'class': 'rank_txt'})

    release_date = movie_title.find_next('div', attrs={'class': 'td'})
    #trailer = release_date.find_next('div', attrs={'class': 'td'})
    # trailer_address = trailer.find('a')['href']
    stars = row.find('h6', attrs={'class': 'count'})

    lastweek_rank = lastweek_rank.string if lastweek_rank.string else ''

    c = [thisweek_rank.string, lastweek_rank, movie_title,
         release_date.string, '', stars.string]
    contents.append(c)


df = pd.DataFrame(contents, columns=colname)
h = df.head(20)
print(h)
