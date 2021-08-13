"""
Dexter Legaspi
Class: CS 521 - Summer 2
Date: 07/21/2021
Term Project
A test for Tkinter
"""
from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.title('doge')
win.geometry("650x400")
path = "data/doge.jpg"
img = ImageTk.PhotoImage(Image.open(path))
label = Label(win, image=img)
label.pack(fill="both", expand="yes")

win.mainloop()
