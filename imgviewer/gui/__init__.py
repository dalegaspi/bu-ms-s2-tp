from tkinter import *
from PIL import ImageTk, Image


def gui_init():
    win = Tk()
    win.title('doge')
    win.geometry("650x400")
    path = "data/doge.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(win, image=img)
    label.pack(fill="both", expand="yes")

    win.mainloop()
