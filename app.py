from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def index():

    dataweb=requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    dateJson=dataweb.json()
    print(dateJson)
    return render_template('index.html',data=dateJson['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 