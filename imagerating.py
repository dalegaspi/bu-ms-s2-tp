"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/04/2021
Term Project
The Image rating class
"""
from tkinter import Tk
import logging

logger = logging.getLogger(__name__)


class ImageRating:
    MAX_RATING = 5
    MIN_RATING = 0

    """
    The image rating
    """

    def __init__(self, rating=MIN_RATING):
        if not ImageRating.__is_valid_rating(rating):
            raise ValueError(
                'Rating must be between {} and {} inclusive'
                .format(ImageRating.MIN_RATING, ImageRating.MAX_RATING))

        self.__rating = rating

    @staticmethod
    def __is_valid_rating(rating: 0):
        return ImageRating.MIN_RATING <= rating <= ImageRating.MIN_RATING

    def get_rating(self):
        return self.__rating

    def __int__(self):
        return self.get_rating()
