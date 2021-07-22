"""
Dexter Legaspi
Class: CS 521 - Summer 2
Date: 07/21/2021
Term Project setup.py
"""

import setuptools

setuptools.setup(
    name='imgviewer',
    version='0.1',
    author="Dexter Legaspi",
    author_email="dalegaspi@gmail.com",
    url="https://github.com/dalegaspi/bu-ms-s2-tp",
    packages=['imgviewer'],
    license='Public Domain',
    long_description=open('README.md').read(),
    entry_points={
        "console_scripts": ["imgviewer=imgviewer:main"]
    }
)
