"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application module entry point
"""
import app
import logging.config
import logging.config

from appglobals import path_config_root_dir

PATH_LOGGING_CONFIG = path_config_root_dir / 'logging.ini'
logging.config.fileConfig(fname=PATH_LOGGING_CONFIG)


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("app entry point")
    app.run()

