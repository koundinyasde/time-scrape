import requests
from bs4 import BeautifulSoup as bs

URL = "https://time.com"
page = requests.get(URL)

soup = bs(page.content, "html.parser")
results = soup.find_all('li', attrs={'class':"latest-stories__item"})

data = []

for i in results:
  headline = i.find("h3", class_="latest-stories__item-headline").text
  time = i.find("time", class_="latest-stories__item-timestamp").text.replace('\\n', '').strip()
  data.append({
    'headline': headline,
    'time': time
  })

print('Latest Stories\n')

for i in range(len(data)):
  print(f'{i+1}.', data[i]['headline'])