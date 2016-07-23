import requests
from bs4 import BeautifulSoup

class BaseScraper(object):
    def __init__(self):
        source_url = None
        html_content = None
        data = []
        params = {}

    def get_source_url(self):
        return self.source_url

    def get_html_content(self):
        page = requests.get(self.get_source_url())
        html_content = BeautifulSoup(page.content, 'lxml')
        self.handle_content(html_content)

    def handle_content(self, html_content):
        raise NotImplementedError("Subclass must implement this to perform parsing with html content from the source url")

    def cleaned_data(self):
        return data
