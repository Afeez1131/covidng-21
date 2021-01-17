from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import requests
import json
from total.models import Total

class Command(BaseCommand):
	help = 'Refresh Database item'

	def handle(self, *args, **options):
		url = 'https://pomber.github.io/covid19/timeseries.json'
		page = requests.get(url)
		try:
			api = json.loads(page.content)
		except Exception as e:
			api = 'Error'
		for ch in api['Nigeria']:
			Total.objects.create(
				day = ch['date'],
				confirmed = ch['confirmed'],
				death = ch['deaths'],
				discharged = ch['recovered'])

		self.stdout.write('Latest Data Fetched')