import requests

from flask import Flask

app = Flask(__name__)

@app.route('/stories')
def getLatestStories():
  print('inside get function')
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
    htmlStr[i] = htmlStr[i].replace('<i>', '').replace('</i>', '').replace('\\', '').replace('</i', '').replace('xe2x80x99', '`')
  return {'data': htmlStr}



# for i in range(len(htmlStr)):
#   print(f'{i+1}.', htmlStr[i])




@app.route('/')
def example():
   return '{"name":"Bob"}'

if __name__ == '__main__':
    try:
      app.run(host='localhost', port=3000)
    except Exception as e:
      print(e)
