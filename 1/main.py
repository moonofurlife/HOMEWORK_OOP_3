import requests
import json

names_of_characters = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
list_of_dictionaries = response.json()

intelligence = []

for i in list_of_dictionaries:
    result = i['powerstats']['intelligence']
    if i['name'] in names_of_characters:
        intelligence.append(result)

full_heroes_list = dict(zip(names_of_characters, intelligence))

maximum = max(full_heroes_list, key = full_heroes_list.get)
print(maximum)