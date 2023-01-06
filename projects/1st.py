import requests
import json

base_url = 'https://animechan.vercel.app/api/quotes'

#title = input('name of anime : ')


r = requests.get(f'{base_url}')
print(r.json())

#quotes = r.json()['quote']
#A_name = r.json()['anime']
#c_name = r.json()['character']
#
#print(f' In {A_name}   {c_name} \n       once said ')
#print(f'{quotes}')