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
from pathlib import Path
import appglobals

logger = logging.getLogger(__name__)


class ImageCatalog:
    """
    The image catalog
    """
    IMAGE_FILESPEC = '*.jpg'

    def __init__(self, directory: str):
        """
        Constructor
        """
        self.__image_path = Path(directory)
        self.__image_files = \
            list(self.__image_path.glob(ImageCatalog.IMAGE_FILESPEC))
        self.__images = ImageCatalog.__build_images(self.__image_files)
        logger.info('catalog has loaded {} files.', len(self.__image_files))
        self.__ratings_path = \
            self.__image_path / appglobals.app_config_ratings_filename

    @staticmethod
    def __build_images(image_files_list: list):
        """
        create a list of records of images from the list of path

        :param image_files_list: image paths
        :return: record list
        """
        # todo maybe optimize by lazy loading the 'img' property
        return [{'path': p, 'img': Image(p)} for p in image_files_list]

    def __len__(self):
        """
        Returns the number of images in the catalog
        :return:
        """
        return len(self.__images)

    def __getitem__(self, item) -> dict:
        """
        return the image at specified index
        :return:
        """
        return self.__images[item]

    def __str__(self):
        """
        str()
        :return:
        """
        return 'Image catalog [{}] has {} images'\
            .format(self.__image_path, len(self.__image_files))

    def get_ratings_path(self):
        """
        Ratings path

        :return:
        """
        return self.__ratings_path

    def get_statistics(self):
        """

        :return:
        """
        # todo use set to create the stats
        pass