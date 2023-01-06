import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
import json

# change coordinates features to place name later 
### reader please do not copy my api key this is starter project 
### if you wish for api key you can get one from the website for free



base_url = ('https://api.openweathermap.org/data/2.5/weather?') 
api_id = '29042c517153ab68f6e2bf1dc490e112'


def search( ):
    lat_cood = entry_lan.get()
    lont_cood = entry_lag.get()
    r = requests.get(f'{base_url}lat={lat_cood}&lon={lont_cood}&appid={api_id}')
    D = r.json()
    condition = D['weather'][0]['description']
    temp = D['main']['temp']
    place = D['name']
    #print(condition , temp ,place)
    temps_lab.config(text = temp)
    condition_lab.config(text = condition)
    cityname_lab.config(text = place)

	



app = Tk()
app.title('weather')
app.geometry('400x400')
entry_lan = Entry(app)
entry_lan.pack(padx=20, pady=8)

entry_lag = Entry(app)
entry_lag.pack(padx=10, pady=10)

search_buttom = Button(app, text='get info', width=12, command=search )
search_buttom.pack()

temps_lab = Label(app,font=('bold', 20 ))
temps_lab.pack()

condition_lab = Label(app, font=('bold', 18))
condition_lab.pack()

cityname_lab = Label(app,  font=('bold',22) )
cityname_lab.pack()


app.mainloop()
