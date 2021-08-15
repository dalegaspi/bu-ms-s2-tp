"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Base Controller
"""
from tkinter import Tk
import logging

from appstate import AppState

logger = logging.getLogger(__name__)


class AppController:
    """
    the application controller
    """
    def __init__(self, state: AppState):
        """
        Constructor

        :param state:
        """
        logger.info('app controller initialized')
        self.__state = state

    @staticmethod
    def copy_to_clipboard(text):
        """
        Copying to clipboard

        https://stackoverflow.com/a/4203897/918858
        :return:
        """
        if len(text) > 0:
            r = Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(text)
            logger.info('setting clipboard value to "%s"', text)
            r.update()
            r.destroy()

    def set_state(self, state: AppState):
        """
        sets app state

        :param state:
        :return:
        """
        self.__state = state

    def get_state(self) -> AppState:
        """
        Return the app state

        :return: the app state
        """
        return self.__state
