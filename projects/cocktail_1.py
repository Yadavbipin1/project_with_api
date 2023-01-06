import requests
import json

base_url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?f='
quary = input('enter the letter you want..')

r = requests.get(f'{base_url}{quary}')

result = r.json()['drinks']
kind = result[0]['strAlcoholic']
instruction = result[0]['strInstructions']

print(f'type : {kind}')
print(f'instructions : {instruction}')
