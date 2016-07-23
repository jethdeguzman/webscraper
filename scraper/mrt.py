import datetime
from .base import BaseScraper
from pytz import timezone

class MrtScraper(BaseScraper):
    source_url = "https://dotcmrt3.gov.ph/service-status"

    def handle_content(self, html_content):
        data = []
        service_date = html_content.find("p", class_="news-main-title").text
        today = datetime.datetime.now(timezone('Asia/Manila'))
        today_minus_4 = today - datetime.timedelta(hours=4)

        if service_date != today.date().strftime('%B %d, %Y'):
            pass

        else:
            service_tbody = html_content.find("table").tbody
            for child in service_tbody.children:
                if not hasattr(child, 'children'): continue
                service_detail = child.contents
                service_time = service_detail[1].text
                service_time_obj = datetime.datetime.strptime(service_time, '%I:%M %p').time()

                if (service_time_obj < today_minus_4.time() or service_time_obj > today.time()):
                    continue

                service_data = {
                    'time' : service_time, 
                    'description' : service_detail[3].text,
                    'status' : service_detail[5].text,
                    'station' : service_detail[7].text.strip(),
                    'bound' : service_detail[9].text
                }

                data.append(service_data.copy())

        self.data = data

