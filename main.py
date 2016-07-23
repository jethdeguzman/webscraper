import json
from flask import Flask, request, Response
from scraper.mmda import MMDAScraper
from scraper.climatex import ClimatexScraper
from scraper.mrt import MrtScraper

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello World!'

@app.route("/api/0/mmda", methods=['POST'])
def mmda():
    data = json.loads(request.data)
    location = data['location'].split('-')

    scraper = MMDAScraper()
    scraper.params = {'main_line' : location[0], 'line_name' : location[1]}
    scraper.get_html_content()
    response_data = {
        'category' : 'traffic',
        'data' : scraper.cleaned_data()
    }
    return json.dumps(response_data)

@app.route("/api/0/climatex", methods=['POST'])
def climatex():
    data = json.loads(request.data)

    scraper = ClimatexScraper()
    scraper.params = {'location' : data['location']}
    scraper.get_html_content()
    response_data = {
        'category' : 'weather',
        'data' : scraper.cleaned_data()
    }
    return json.dumps(response_data)

@app.route("/api/0/mrt", methods=['GET'])
def mrt():
    scraper = MrtScraper()
    scraper.get_html_content()
    response_data = {
        'category' : 'mrt',
        'data' : scraper.cleaned_data()
    }
    return json.dumps(response_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
