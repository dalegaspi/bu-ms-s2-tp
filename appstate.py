"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application main app that builds the MVC
"""
import sys

from imagecatalog import ImageCatalog
import logging

logger = logging.getLogger(__name__)


class AppState:
    """
    The application state
    """

    MIN_INDEX = 0

    def __init__(self, catalog: ImageCatalog = None, max_index=sys.maxsize):
        """
        Constructor

        :param catalog: the image catalog
        :param max_index: max index if image catalog is None
        """
        self.__image_catalog: ImageCatalog = catalog
        self.__image_index = AppState.MIN_INDEX
        self.__max_index = max_index if self.__image_catalog is None \
            else len(self.__image_catalog) - 1

    def __iadd__(self, other: int):
        """
        Fancy way to increment current index

        :param other: the int operand
        :return: self
        """
        if self.__image_index < self.__max_index:
            self.__image_index += other
        else:
            self.__image_index = AppState.MIN_INDEX

        return self

    def __isub__(self, other: int):
        """
        Fancy way to decrement current index

        :param other: the int operand
        :return: self
        """
        if self.__image_index > AppState.MIN_INDEX:
            self.__image_index -= other
        else:
            self.__image_index = self.__max_index

        return self

    def reset(self):
        """
        reset the app state index

        :return:
        """
        self.__image_index = AppState.MIN_INDEX

    def get_max_index(self):
        """
        get the max index

        :return:
        """
        return self.__max_index

    def get_index(self):
        """
        get the current index

        :return:
        """
        return self.__image_index

    def get_catalog(self) -> ImageCatalog:
        """
        get the image catalog

        :return:
        """
        return self.__image_catalog

    def has_catalog(self):
        """
        returns true if there is a catalog

        :return:
        """
        return self.__image_catalog is not None

    def __str__(self):
        """
        Return application state in human-readable form
        
        :return:
        """
        return 'Application state current_index: {}, ' \
               'max_index: {}, has_catalog: {}'.format(self.get_index(),
                                                       self.get_max_index(),
                                                       self.has_catalog())
