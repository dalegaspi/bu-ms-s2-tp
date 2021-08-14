"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/26/2021
Term Project
Image utility classes/defs
"""
from PIL.Image import Exif
import PIL.ExifTags

# constants for EXIF tags we are interested in
EXIF_FNUMBER = 'FNumber'
EXIF_ISO = 'ISOSpeedRatings'
EXIF_EXPOSURE = 'ExposureTime'
EXIF_MAKE = 'Make'
EXIF_MODEL = 'Model'
EXIF_TAGS_OF_INTEREST = [
    EXIF_FNUMBER,
    EXIF_ISO,
    EXIF_MAKE,
    EXIF_MODEL,
    EXIF_EXPOSURE]


class ImageAttributes:
    """
    A convenience class for EXIF
    """

    def __init__(self, image: PIL.Image.Image):
        self.image = image
        # noinspection PyProtectedMember
        self.exif = image._getexif()
        self.__parse_exif()

    def __parse_exif(self):
        """
        parses exif then stores internally in attr_dict

        :return:
        """
        self.attr_dict = {}
        for k in EXIF_TAGS_OF_INTEREST:
            try:
                self.attr_dict[k] = self.exif[
                    ImageAttributes.exif_attribute_as_index(k)]
            except (KeyError, Exception):
                pass

    @staticmethod
    def exif_attribute_as_index(attribute_name):
        """
        PIL.ExifTags.TAGS is a dictionary of indices with corresponding names.
        This is a convenience function that returns the EXIF index for
        the corresponding name to lessen the confusion

        :param attribute_name:
        :return:
        """
        index = next(k for k, v in PIL.ExifTags.TAGS.items()
                     if v.lower() == attribute_name.lower())
        return index

    def __attr_dict_as_string(self):
        """
        return the EXIF as a newline separated key-value pairs

        :return:
        """
        return 'No EXIF Data' if len(self.attr_dict) == 0 \
            else '\n'.join([f'{k}: {v}' for k, v in self.attr_dict.items()])

    def get_formatted_exif(self):
        """
        get the formatted version of exif

        :return:
        """
        return str(self.__attr_dict_as_string())

