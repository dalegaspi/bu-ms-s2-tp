"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/04/2021
Term Project
The Image class
"""
from pathlib import Path
from tkinter import Tk
from PIL import Image as PILImage
import logging

from imageattributes import ImageAttributes
from imagerating import ImageRating

logger = logging.getLogger(__name__)


class Image:
    """
    The image
    """
    def __init__(self, path: str, rating: ImageRating = None):
        self.__path = Path(path)
        self.__name = self.__path.name
        self.__read_image_attributes()
        self.__rating: ImageRating = rating

    def __read_image_attributes(self):
        img = self.get_image_object()
        self.__attr = ImageAttributes(img)
        img.close()

    def get_image_object(self) :
        return PILImage.open(self.__path)

    def set_rating(self, rating: ImageRating):
        self.__rating = rating

    def get_rating(self):
        return self.__rating

    def get_attributes(self):
        return self.__attr

    def get_name(self):
        return self.__name


