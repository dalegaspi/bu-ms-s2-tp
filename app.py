"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application main app that builds the MVC
"""
from basecontroller import BaseController
from constants import APP_CONFIG
from mainview import render_main_view
import logging

logger = logging.getLogger(__name__)


def dump_configuration():
    """
    dumps the app configuration in log
    :return:
    """
    for skey, svalue in APP_CONFIG.items():
        for key, value in svalue.items():
            logger.info("%s:%s = %s", skey, key, value)


def run():
    dump_configuration()
    base_controller = BaseController()
    BaseController.copy_to_clipboard('hello')
    render_main_view(controller=base_controller)


