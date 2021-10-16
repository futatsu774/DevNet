from tkinter import *
import tkinter
from requests import get
import json

ip = get('https://ip4.seeip.org').text
geo= get('https://ip.seeip.org/geoip').text

sample =Tk()
sample.title("IP Getter")
sample.geometry("900x300")

json_str = json.dumps(geo)

resp=json.loads(json_str)

def setIP(text):
    textExample.delete(0,"end")
    textExample.insert(0,text)

def setGeo(text):
    
    inputtxt.insert(END,text)

# textExample2 = tkinter.Entry(sample)
# textExample2.pack()

textExample = tkinter.Entry(sample,justify="center")
textExample.pack(padx=300,pady=10)

inputtxt = Text(sample, height = 30,
                width = 50,
                bg = "light yellow")                
inputtxt.pack(padx=300, pady=40)



IPbutton = tkinter.Button(sample, text="Get IP", width=10, command = lambda:setIP(ip))
IPbutton.place(x=405, y=35)

Geobutton = tkinter.Button(sample, text="Get Geo Location", width=15, command = lambda:setGeo(resp))
Geobutton.place(x=385,y=265)


sample.mainloop()



# print (resp,)



