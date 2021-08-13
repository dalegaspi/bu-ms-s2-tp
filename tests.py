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

    def test_creation(self):
        c = BaseController()
        self.assertIsNotNone(c)
