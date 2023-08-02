from tkinter import Tk
from tkinter import Label
from time import *
from sys import *

dev = 'Kevin O.O '
timescreen = Tk()
timescreen.title('Digital Clock - Time Check: Brought To You By ' + dev)
timescreen.geometry('700x300')

def what_time():

    currtime = strftime('%I:%M:%S %p')
    timedis.config(text = currtime)
    timedis.after(200 , what_time)

timedis = Label(timescreen, font = ('roman', 90 ), bg= 'black' , fg = 'white' )
timedis.pack()

what_time()

timescreen.mainloop()
