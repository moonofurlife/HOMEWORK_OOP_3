import requests
import datetime
import json

two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)

url = 'https://api.stackexchange.com/2.3/questions'
params = {
    'fromdate': int(two_days_ago.timestamp()),
    'tagged': 'python',
    'site': 'stackoverflow',}
response = requests.get(url, params=params)
for item in response.json()['items']:
    print(item['title'])