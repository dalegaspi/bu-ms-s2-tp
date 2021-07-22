"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application main app that builds the MVC
"""
from imgviewer.controllers.base import BaseController
from imgviewer.views.main import MainView
import logging

logger = logging.getLogger(__name__)


def run():
    main_view = MainView()
    logger.info("hello from app.main()")
    BaseController.copy_to_clipboard('hello')
    main_view.run()
