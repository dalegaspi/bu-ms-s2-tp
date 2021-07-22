# CS521 Term Project

This project showcases what was learned in CS521 class.  

## Description and Features

This is an Image Viewer that allows user to select a directory and display all the images in said directory in a carousel-like fashion with its EXIF, and be able to optionally rate the images.  the image ratings are saved in a CSV in the same directory where the images are located.

## Technology Stack

- Python 3.x
- Tkinter
- Pillow

## Application Design

The application adheres to the principles of the [Model-View-Controller design pattern](https://en.wikipedia.org/wiki/Model–view–controller).  The image entities and the catalog are represented as Model classes, the views/windows/widgets are represented as View classes and are glued together by the Controller classes.

## Running the Application

### Configuration

The application and logging configuration is under the `config/` directory named `app.ini` and `logging.ini`, respectively.

### Dependencies

Make sure you install the dependencies listed in `requirements.txt`.  To install using `pip`:

```shell
$ pip install -r requirements.txt
```

The app should be run as a python module.  The `PYTHONPATH` environment variable so the modules 

```shell
$ cd imgviewer/
$ export PYTHONPATH=`pwd`
$ python -m imgviewer
```

## Running the unit tests

Running the unit tests using the standard `unittest` module is no different here.  The unit tests are located in the `/tests` sub-directory and it will discover and automatically run the tests and display the results

```shell
$ cd tests/
$ python -m unittest -v
```

## Troubleshooting

if this error is displaye while running the app:

```shell
Traceback (most recent call last):
  File "/Users/dexter/Projects/CS521/bu-ms-s2-tp/tkinter_test.py", line 8, in <module>
    from tkinter import *
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/tkinter/__init__.py", line 36, in <module>
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter'
```

This means Tkinter is not available either use pip3 to install tk manually
```shell

> pip3 install tk

# or

> brew install python-tk

```

