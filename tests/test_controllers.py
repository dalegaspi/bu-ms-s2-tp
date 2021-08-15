"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Controller unit tests
"""
import unittest

from appcontroller import AppController
from appstate import AppState


class ControllerTests(unittest.TestCase):
    """
    Tests for controller
    """

    def setUp(self) -> None:
        """
        Setup

        :return:
        """
        self.appstate = AppState()
        self.controller = AppController(self.appstate)

    def test_creation(self):
        """
        Test creation of controller
        """
        self.assertIsNotNone(self.controller)
        self.assertEqual(self.controller.get_state(), self.appstate)

    def test_operations(self):
        """
        test controller operations
        """
        img = self.controller.get_image_at_current_index()
        self.assertIsNone(img)

        self.controller.next_image()
        self.assertTrue(self.appstate.get_index() == AppState.MIN_INDEX)

        self.controller.previous_image()
        self.assertTrue(self.appstate.get_index() == AppState.MIN_INDEX)
