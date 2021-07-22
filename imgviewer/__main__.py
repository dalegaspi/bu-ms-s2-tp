"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Application module entry point
"""
import app
import logging.config


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("app entry point")
    app.run()
