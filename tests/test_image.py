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


class ImageTests(unittest.TestCase):
    """
    Images tests
    """
    IMAGE_SAMPLE = Path(os.path.dirname(os.path.abspath(__file__))) \
        / "data" / "flower_big.jpg"

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