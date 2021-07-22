"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Initialization of module
"""
import logging.config

from imgviewer.utils import ROOT_DIR

logging.config.fileConfig(fname=f'{ROOT_DIR}/imgviewer/config/logging.ini')


