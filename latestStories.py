import requests
URL = "https://time.com"
page = requests.get(URL)
htmlStr = str(page.content)

ind = htmlStr.index('class="partial latest-stories"')
htmlStr =  htmlStr[ind:]

ind2 = htmlStr.index('</section>')
htmlStr=htmlStr[:ind2]

htmlStr = htmlStr[htmlStr.index('<li'):].strip('<li')
htmlStr = htmlStr.split('<li')
for i in range(len(htmlStr)):
  htmlStr[i] = htmlStr[i][htmlStr[i].index('<h3'):].strip('<h3')
  htmlStr[i] = htmlStr[i][htmlStr[i].index('item-headline">'):].strip('item-headline">')
  htmlStr[i] = htmlStr[i][:htmlStr[i].index('</h3>')].strip('</h3>')
  htmlStr[i] = htmlStr[i].replace('<i>', '').replace('</i>', '').replace('\\', '').replace('</i', '')

print('Latest Stories\n')

for i in range(len(htmlStr)):
  print(f'{i+1}.', htmlStr[i])
