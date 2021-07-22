"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Main view/window
"""
from tkinter import *
from PIL import ImageTk, Image, ExifTags
import logging

from imgviewer import ROOT_DIR

logger = logging.getLogger(__name__)


class MainView:
    def __init__(self):
        pass

    def run(self):
        """
        :return:
        """
        win = Tk()
        win.title('doge')
        win.geometry('650x400')
        path = f'{ROOT_DIR}/imgviewer/data/flower_big.jpg'
        img = Image.open(path)

        # this is a test for resizing
        # https://stackoverflow.com/a/24745969/918858

        maxsize = (400, 300)
        img.thumbnail(maxsize, Image.ANTIALIAS)

        pimg = ImageTk.PhotoImage(img)
        exif = img.getexif()
        win.title(img.getexif())
        label = Label(win, image=pimg)
        label.pack(fill="both", expand="yes")

        win.mainloop()
