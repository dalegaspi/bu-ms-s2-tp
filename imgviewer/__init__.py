"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Initialization of module
"""
import logging.config

from imgviewer.utils import PATH_CONFIG_ROOT_DIR

PATH_LOGGING_CONFIG = PATH_CONFIG_ROOT_DIR / 'logging.ini'
logging.config.fileConfig(fname=PATH_LOGGING_CONFIG)
