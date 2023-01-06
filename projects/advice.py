import requests
import json

base_url = 'https://api.adviceslip.com/advice/'
slip_id = input('enter the number of the advice.. ')
r = requests.get(f'{base_url}{slip_id}')

result = r.json()['slip']
sugest = result['id']
adv = result['advice']

print(f'{sugest}:- {adv}')
