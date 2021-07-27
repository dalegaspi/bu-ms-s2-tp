"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application constants, utils and helpers
"""
import os
from configparser import ConfigParser
from pathlib import Path

# this is the root directory of the module
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_ROOT_DIR = Path(ROOT_DIR)

# data directory
PATH_DATA_ROOT_DIR = PATH_ROOT_DIR / 'imgviewer' / 'data'

# config directory
PATH_CONFIG_ROOT_DIR = PATH_ROOT_DIR / 'imgviewer' / 'config'

# application configuration
APP_CONFIG = ConfigParser()
APP_CONFIG.read(PATH_CONFIG_ROOT_DIR / 'app.ini')
