import tkinter as tk
from requests import get

ip = get('https://api.ipify.org').text

sample =tk.Tk()
sample.title("IP Getter")
sample.geometry("250x100")

def setTextInput(text):
    textExample.delete(0,"end")
    textExample.insert(0,text)

textExample = tk.Entry(sample)
textExample.pack()

button = tk.Button(sample, text="Get IP", width=10, command = lambda:setTextInput(ip))
button.place(x=90, y=30)

sample.mainloop()



