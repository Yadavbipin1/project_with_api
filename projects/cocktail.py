import requests
import json

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?s='
quary = input('please input a drink to search  ')

r = requests.get(f'{base_url}{quary}')
result = r.json()['drinks']
instruction = result[0]['strInstructions']
print(f'instruction: {instruction} ')
