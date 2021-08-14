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
root_dir = os.path.dirname(os.path.abspath(__file__))
path_root_dir = Path(root_dir)

# data directory
path_data_root_door = path_root_dir / 'data'

# config directory
path_config_root_dir = path_root_dir / 'config'

# application configuration
app_config = ConfigParser()
app_config.read(path_config_root_dir / 'app.ini')

app_config_win_dimension = (app_config.getint('window', 'width'),
                            app_config.getint('window', 'height'))

app_config_img_dimension = (app_config.getint('image', 'width'),
                            app_config.getint('image', 'height'))

app_config_confirm_on_exit = app_config.getboolean('app', 'confirmonexit')

app_config_ratings_filename = app_config.get('catalog', 'ratingsfilename')
