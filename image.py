"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/04/2021
Term Project
The Image class
"""
import logging
from pathlib import Path
from PIL import Image as PILImage
from imageattributes import ImageAttributes
from imagerating import ImageRating

logger = logging.getLogger(__name__)


class Image:
    """
    The image
    """
    def __init__(self, path: str, rating: ImageRating = None):
        """
        Constructor

        :param path: absolute path
        :param rating: rating
        """
        self.__path = Path(path)
        self.__name = self.__path.name.lower()
        self.__read_image_attributes()
        self.__rating: ImageRating = rating

    def __read_image_attributes(self):
        """
        read the EXIF into self.__attr

        :return: None
        """
        img = self.get_image_object()
        self.__attr = ImageAttributes(img)
        img.close()

    def get_image_object(self):
        """
        Return the PIL Image

        :return: the image
        """
        return PILImage.open(self.__path)

    def set_rating(self, rating: ImageRating):
        """
        Set rating

        :param rating:
        :return: None
        """
        self.__rating = rating

    def get_rating(self):
        """
        Get rating

        :return: the rating
        """
        return self.__rating

    def get_attributes(self):
        """
        get the image attributes

        :return: the image attributes
        """
        return self.__attr

    def get_name(self):
        """
        get the short name (based on file path)

        :return: the short name
        """
        return self.__name


