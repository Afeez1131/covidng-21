from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import requests
import json
from datetime import date
from total.models import Total

class Command(BaseCommand):
	help = 'Refresh Database item'

	def handle(self, *args, **options):
		year_digit = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr':4, 'May':'5', 'Jun':'6', 'Jul':'7', 'Aug':'8', 'Sep':'9', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
		url = requests.get('https://covid19.ncdc.gov.ng/')

		soup = BeautifulSoup(url.content, 'html.parser')
		custom1 = soup.find(class_ = 'text-right text-white')

		confirmed_cases = custom1.text
		active_cases = soup.find_all('h2')
		# date = date.string

		confirmed = active_cases[1].text 
		discharged = active_cases[3].text
		death = active_cases[4].text 

		da = str(date.today())

		y = da.split('-')[0]
		m = da.split('-')[1]
		d = da.split('-')[2]

		if d.startswith('0'):
			m = m.strip('0')

		day = y + '-' + m + '-' + d
		confirmed = confirmed
		discharged = discharged
		death = death

		print(day, confirmed, discharged, death)
		Total.objects.create(
			day = day,
			confirmed=confirmed,
			discharged=discharged,
			death=death
			)

		self.stdout.write('latest data fetched')