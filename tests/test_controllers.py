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

    def setUp(self) -> None:
        """
        Setup

        :return:
        """
        self.controller = BaseController()

    def test_creation(self):
        """
        Test creation of controller
        """
        self.assertIsNotNone(self.controller)

