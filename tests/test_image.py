"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/14/2021
Term Project
Image unit tests
"""
import os
import unittest
from pathlib import Path

from image import Image
from imageattributes import ImageAttributes
from imagerating import ImageRating


class ImageTests(unittest.TestCase):
    """
    Images tests
    """
    IMAGE_SAMPLE = Path(os.path.dirname(os.path.abspath(__file__))) \
        / "data" / "L1000191.jpg"

    def setUp(self) -> None:
        """
        Setup

        :return:
        """
        self.image = Image(str(ImageTests.IMAGE_SAMPLE))

    def test_image_properties(self):
        """
        Test image properties

        :return:
        """
        self.assertIsNotNone(self.image)

    def test_image_rating(self):
        """
        test image rating

        :return:
        """
        rating = ImageRating(4)
        self.assertEqual(int(rating), 4)

    def test_invalid_rating(self):
        """
        test image invalid rating

        :return:
        """
        self.assertRaises(ValueError, ImageRating, 7)

    def test_image_attributes(self):
        """
        test image attributes

        :return:
        """
        attr = ImageAttributes(self.image.get_image_object())
        self.assertIsNotNone(attr)
        self.assertTrue(len(attr.attr_dict) > 0)
        self.assertTrue(len(attr.get_formatted_exif()) > 0)
