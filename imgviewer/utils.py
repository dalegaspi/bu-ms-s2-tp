"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application constants, utils and helpers
"""
import os
from configparser import ConfigParser

# this is the root directory of the module where all other resource paths will be based from
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# application configuration
APP_CONFIG = ConfigParser()
APP_CONFIG.read(f'{ROOT_DIR}/imgviewer/config/app.ini')
