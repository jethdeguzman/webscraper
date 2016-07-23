from .base import BaseScraper

class ClimatexScraper(BaseScraper):
    source_url = "http://climatex.dost.gov.ph/predict.html"

    def handle_content(self, html_content):
        data = []
        data_table = html_content.find("table")
        for tr in data_table.find_all('tr'):
            data_item = {}
            for i, td in enumerate(tr.children):
                if not hasattr(td, 'children') or (i != 1 and i != 3) : continue 
                if i == 1:
                    if not hasattr(td.strong, 'font'): continue
                    if not td.strong.font.text: continue
                    data_item['location'] = td.strong.font.text
                if i == 3:
                    if not hasattr(td.center, 'font'): continue
                    if not td.center.font.text: continue
                    data_item['chance_of_rain'] = td.center.font.text
            data.append(data_item.copy())

        self.data = filter(None, data)

    def cleaned_data(self):
        return [item for item in self.data if self.params['location'].lower() in item['location'].lower()]
