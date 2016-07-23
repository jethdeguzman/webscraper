FROM python:2.7
COPY requirements.txt /webscraper/
RUN pip install -r /webscraper/requirements.txt
COPY . /webscraper/
WORKDIR /webscraper
EXPOSE  5000
CMD ["uwsgi", "--ini", "uwsgi.ini"]
