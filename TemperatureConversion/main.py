#import tkinter
from tkinter import *

window = Tk()
window.title("Temperature Conversion")
window.geometry("900x300")

#defined a function
def conversion():

#formula for celsius to fahrenheit
    if cel:
        celToFah = float(celsius.get())
        answer = (celToFah * 9 / 5 + 32)
        lbans.config(text=round(answer, 2))
#formula for fahrenheit to celsius
    elif fah:
        fahToCel = float((fahrenheit.get()))
        answer2 = ((fahToCel - 32) * (5 / 9))
        lbans.config(text=round(answer2, 2))

#conversion button
convert = Button(window, text="Convert", relief=RAISED, command=conversion)
convert.grid(row=2, column=0, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

#define a function for clear
def clear():
    fahrenheit.set(int(0))
    celsius.set(int(0))
    cel.config(state=DISABLED)
    fah.config(state=DISABLED)
    lbans.configure(text="")

clear = Button(window, text="Clear", relief=RAISED, command=clear)
clear.grid(row=1, column=2, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

#activation functions
def activate_c():
    cel.config(state=NORMAL)


def activate_f():
    fah.config(state=NORMAL)

#exit function
def exit_window():
    window.destroy()


button = Button(text="exit", command=exit_window)
button.grid(row=2, column=2)

celsius = IntVar()
celsius.set(int(0))
fahrenheit = IntVar()
fahrenheit.set(int(0))



#c to f
lbframe = LabelFrame(window, text="Celsius to fahrenheit")
lbframe.grid(row=0, column=0, pady=10, padx=20, sticky=NW)



cel = Entry(lbframe, state=DISABLED, textvariable=celsius)
cel.grid(row=1, column=3)

activateC = Button(window, text="Activate Celsius to Fahrenheit", command=activate_c)
activateC.grid(row=1, column=0)


#f to c
lbframe2= LabelFrame(window, text="Fahrenheit to Celsius")
lbframe2.grid(row=0, column=6)

fah= Entry(lbframe2,state=DISABLED, textvariable= fahrenheit)
fah.grid(row=0, column=6)

activateF = Button(window, text="Activate Fahrenheit to Celsius", command=activate_f)
activateF.grid(row=1, column=6)


lbans=Label(window, text="", bg="grey", width=20)
lbans.grid(row=2, column=1)



window.mainloop()
