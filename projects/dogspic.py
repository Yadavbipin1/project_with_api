import requests
import json
import webbrowser as wb


##https://random.dog/0a2599dd-86b4-49a4-acf4-254705442e3d.mp4
##this is funny


url = 'https://random.dog/woof.json'

r_get = requests.get(url)

r = r_get.json()
#print(r)

data = r['url']
#print(data)

wb.open(data)