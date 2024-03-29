"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application main app that builds the MVC
"""
from appcontroller import AppController
from appglobals import app_config
from appstate import AppState
from mainview import render_main_view
import logging

logger = logging.getLogger(__name__)


def dump_configuration():
    """
    Dumps the app configuration in log
    :return:
    """
    for skey, svalue in app_config.items():
        for key, value in svalue.items():
            logger.info("%s:%s = %s", skey, key, value)


def run():
    """
    Initialize and runs the app (blocks until the GUI is destroyed)
    :return:
    """
    dump_configuration()
    state = AppState()
    controller = AppController(state)
    AppController.copy_to_clipboard('hello')
    render_main_view(controller=controller)


