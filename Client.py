#!/usr/bin/env python
# -*- coding: utf-8 -*-


# importing tkinter for gui

from tkinter import * 
from tkinter.ttk import *
import datetime
import requests
from datetime import datetime
from playsound import playsound
import time

def play():
    
    playsound('1.mp3')

def get_internet_datetime(time_zone: str = "America/Santiago") -> datetime:
    """
    Get the current internet time from:
    'https://www.timeapi.io/api/Time/current/zone?timeZone=etc/utc'
    """

    timeapi_url = "https://www.timeapi.io/api/Time/current/zone"
    headers = {
        "Accept": "application/json",
    }
    params = {"timeZone": time_zone}

    dt = None
    try:
        request = requests.get(timeapi_url, headers=headers, params=params)
        r_dict = request.json()
        dt = datetime(
            year=r_dict["year"],
            month=r_dict["month"],
            day=r_dict["day"],
            hour=r_dict["hour"],
            minute=r_dict["minute"],
            second=r_dict["seconds"],
            microsecond=r_dict["milliSeconds"] * 1000,
        )
        print("Usando Tiempo Internet")
    except Exception:
        print('Usando hora PC')
        now = datetime.datetime.now()
        return now

    return dt

def on_closing():
        newWindow.withdraw()

def Secondwindow():
    print('entro')
    newWindow.deiconify()
   
   


def primerrelay(state):
    print('entrando a primer relay')
    with open("tiempo.txt",'r') as f:
        p = f.read()
        numeros = p.split(";")
        num = [int(x) for x in numeros]
    checktime(state,num)
    
def checktime(state,num):
    now = get_internet_datetime()
    
    #now = datetime.datetime.now()
    if now.hour == num[0] and (now.minute > num[1] and now.minute < num[2]) :
        
        if newWindow.state() == 'withdrawn' and state == 'vacio':
                state ='usado'
                print(now.hour,now.minute)
                Secondwindow()
                play() 
                timeval = 15000
        elif newWindow.state() == 'zoomed': 
                timeval = 15000
                play()
        else:
            timeval =100000


    else:
        timeval =100000
        print('Fuera de tiempo')
        state = 'vacio'

    window.after(timeval,checktime,state,num)

        
 


# creating window
state ='vacio'
window = Tk()
window.withdraw()
newWindow = Toplevel(window)
newWindow.withdraw()
    # setting attribute
newWindow.attributes('-fullscreen', True)
newWindow.attributes('-topmost', True)
newWindow.title("Recordatorio Lista")
label = Label(newWindow, text="Pasar Lista!")
label.pack()
photo = PhotoImage(file = r"1999053.png")
Button(newWindow, text = 'Click Me !', image = photo, command=on_closing).pack(side = TOP)

window.after(5000, primerrelay,state)
window.mainloop()







