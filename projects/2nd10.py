import requests
import json

url = 'https://animechan.vercel.app/api/quotes'
url1 = 'https://animechan.vercel.app/api/quotes/anime?title='
title = input('enter the name of anime: ')
if title == '':
    r_get = requests.get(f'{url}')
else:
    r_get = requests.get(f'{url1}{title}')    


r = r_get.json

i = 0 
while i < 10:
    print(f"once {r()[i]['character']} said in {r()[i]['anime']}")
    print(f"--->{r()[i]['quote']}")    
    i = i + 1
