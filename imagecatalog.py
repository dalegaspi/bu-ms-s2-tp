"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/04/2021
Term Project
The Image Catalog class
"""
from tkinter import Tk
import logging

from image import Image

logger = logging.getLogger(__name__)


class ImageCatalog:
    """
    The image catalog
    """
    def __init__(self):
        """
        Constructor
        """
        self.__images_count = 0

    def __len__(self):
        """
        Returns the number of images in the catalog
        :return:
        """
        return self.__images_count

    def __index__(self) -> Image:
        """
        return the image at specified index
        :return:
        """
        return None

    def __str__(self):
        pass
