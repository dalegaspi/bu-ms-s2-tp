"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Controller unit tests
"""
import unittest

from basecontroller import BaseController


class ControllerTests(unittest.TestCase):
    """
    Tests for controller
    """

    def test_creation(self):
        """
        Test creation of controller
        """
        c = BaseController()
        self.assertIsNotNone(c)

    def test_assert(self):
        """
        Test assertion

        :return:
        """
        self.assertTrue(True)
