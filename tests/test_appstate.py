"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 08/14/2021
Term Project
App state unit tests
"""
import unittest

from appstate import AppState


class AppStateTests(unittest.TestCase):
    """
    Tests for app state
    """

    def setUp(self) -> None:
        """
        setup

        :return:
        """
        self.app_state = AppState(max_index=10)

    def test_index_operations(self):
        """
        app state index operation tests

        :return:
        """
        self.app_state += 1
        self.assertTrue(self.app_state.get_index() == 1)

        self.app_state.reset()

        self.app_state += 10
        self.app_state -= 1
        self.assertTrue(self.app_state.get_index() == 9)

        # the next couple of tests should not have index go
        # beyond 0 <= index < max_index
        self.app_state.reset()
        self.app_state -= 1
        self.assertTrue(
            self.app_state.get_index() == self.app_state.get_max_index())

        self.app_state += 1
        self.assertTrue(self.app_state.get_index() == AppState.MIN_INDEX)
