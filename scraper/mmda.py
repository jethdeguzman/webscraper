from .base import BaseScraper

class MMDAScraper(BaseScraper):
    def handle_content(self, html_content):
        data = []
        line_table = html_content.find("div", class_="line-table")
        
        for i, line in enumerate(line_table.children):
            if not hasattr(line, 'children') or i == 1: continue
            north_bound = {}
            south_bound = {}
            line_name = line.find_all('div', 'line-name')[0].p.a.text
            line_col = line.find_all('div', 'line-col')
            south_bound['status'] = line_col[0].find('div', 'line-status').contents[3].text
            south_bound['datetime'] = line_col[0].find('p').text.replace('Updated', '')
            north_bound['status'] = line_col[1].find('div', 'line-status').contents[3].text
            north_bound['datetime'] = line_col[0].find('p').text.replace('Updated', '')
            line_data = {'name' : line_name, 'south_bound' : south_bound, 'north_bound' : north_bound}
            data.append(line_data.copy())

        self.data = data

    def get_source_url(self):
        return "http://mmdatraffic.interaksyon.com/line-view-%s.php" % (self.params['main_line'].lower())

    def cleaned_data(self):
        line_name = self.params['line_name']
        return [item for item in self.data if line_name.lower() in item['name'].lower()]
