"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Base Controller
"""
from tkinter import Tk


class BaseController:

    @staticmethod
    def copy_to_clipboard(text='clipboards are 4eva'):
        """
        Copying to clipboard

        https://stackoverflow.com/a/4203897/918858
        :return:
        """
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()
