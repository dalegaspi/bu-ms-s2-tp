"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application main app that builds the MVC
"""
from basecontroller import BaseController
from appglobals import app_config
from mainview import render_main_view
import logging

logger = logging.getLogger(__name__)


class AppState:
    """
    The application state
    """
    def __init__(self):
        pass