from urllib import response
import requests
import json

r = requests.get('https://api.chucknorris.io/jokes/random')

dic = r.json()

stlye = dic['value']
print(f'joke.... {stlye}')
