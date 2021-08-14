"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/14/2021
Term Project
Catalog unit tests
"""
import os
import unittest
from pathlib import Path

from imagecatalog import ImageCatalog


class ImageCatalogTests(unittest.TestCase):
    """
    Tests for image catalog
    """
    IMAGE_DIRECTORY = Path(os.path.dirname(os.path.abspath(__file__))) / "data"

    def setUp(self) -> None:
        self.catalog = ImageCatalog(
            directory=str(ImageCatalogTests.IMAGE_DIRECTORY))

    def test_catalog_properties(self):
        """
        Test image catalog properties
        :return:
        """
        self.assertIsNotNone(self.catalog.get_ratings_path())

    def test_listing(self):
        """
        Test image catalog listing
        :return:
        """
        self.assertTrue(len(self.catalog) > 0)

    def test_index_retrieval(self):
        """
        Test getting image at specified index

        :return:
        """
        img = self.catalog[0]
        self.assertIsNotNone(img)

    def test_save_ratings(self):
        """
        test saving of ratings

        :return:
        """
        self.assertTrue(self.catalog.save_ratings())

    def test_get_stats(self):
        """
        statistics test

        :return:
        """
        stats = self.catalog.get_stats()
        self.assertTrue(len(stats) > 0)
