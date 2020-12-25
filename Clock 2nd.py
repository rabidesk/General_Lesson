from tkinter import *
from time import *

def update():
    timeString = strftime("%I:%M:%S %p")
    label.config(text=timeString)
    label.after(1000,update)


window = Tk()
label = Label(window,font=("Arial",50),fg="#00FF00",bg = "black")
label.pack
update()


window.mainloop()