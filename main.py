from flask import Flask, render_template
app = Flask(__name__)
import requests
import json
import time
URL = " https://api.thingspeak.com/channels/1352554/feeds.json?results=10"
@app.route("/")
def index():
    while True:
        res = requests.get(url = URL)
        resp_json = res.json()
        data = resp_json.get("feeds")
        return render_template('index.html', data_fetch = data)
if __name__ == "__main__":
   app.run(debug=True)