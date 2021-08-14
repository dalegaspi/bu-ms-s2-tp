# CS521 Term Project

This project showcases what was learned in CS521 class.  

## Description and Features

This is an Image Viewer that allows user to select a directory and display all the images in said directory in a carousel-like fashion with its EXIF, and be able to optionally rate the images.  the image ratings are saved in a CSV in the same directory where the images are located.

## Technology Stack

- Python 3.x
- Tkinter
- Pillow

## Code Structure and Dependencies

The application is meant as an exercise rather than a true installable module, hence it is following a much simplified code structure as described in [this article](https://realpython.com/python-application-layouts/#one-off-script).  The required modules/dependencies are in a standard `requirements.txt` file and can be easily installed using `pip`:

```shell
$ pip install -r requirements.txt
```

## Application Design

The application adheres to the principles of the [Model-View-Controller design pattern](https://en.wikipedia.org/wiki/Model–view–controller).  The image entities and the catalog are represented as Model classes, the views/windows/widgets are represented as View classes and are glued together by the Controller classes.

## Running the Application

`imageviewer.py` is the application's entry point, it can be run simply in the project's current directory by:

```shell
$ python imageviewer.py
```

### Application and Logging Configuration(s)

The application and logging configuration is under the `config/` directory named `app.ini` and `logging.ini`, respectively.

## Unit Testing

[Running the unit tests using the standard `unittest` module](https://docs.python.org/3/library/unittest.html) is no different here.  The unit tests are located `tests` directory but the `unittest` module will discover and automatically run the tests and display the results without having to explicitly specify the unit test files:

```shell
$ python -m unittest discover tests -v
```

## Project Term Requirements

Below is the table outlining the project term requirements and how they were met:

| Requirement    | Remarks     |
|----------------|-------------|
| Dictionary | `ImageCatalog::__image_records` in `imagecatalog.py` is a list of dictionaries |
| List | `ImageCatalog::__image_records` in `imagecatalog.py` is a list of dictionaries |
| Set | `ImageCatalog::get_stats()` returns a set with the unique camera brands used to create the images in the catalog in `imagecatalog.py`
| Tuple | `app_config_win_dimension` and `app_config_img_dimension` global variables defined in `appglobals.py` |
| Iteration Type | `ImageCatalog::load_ratings()` in `imagecatalog.py`
| Conditional | `ImageRating::__init__()` in `imagerating.py` |
| Try-Block with Else Condition | `ImageCatalog::save_ratings()` in `imagecatalog.py` |
| User-Defined Function | `dump_configuration()` and `run()` in `app.py`|
| Input/Output File | Use of `_ratings.dat` file in `ImageCatalog` class in `imagecatalog.py`|
| Class with 1 private, 2 public `self` attributes | `__image_records`, `image_path` and `image_files` in `ImageCatalog` in `imagecatalog.py` |
| Class with 1 private and 1 public method that take arguments, return values and are used by your program | `ImageCatalog::__apply_ratings()` and `ImageCatalog::set_rating()` in `imagecatalog.py` |
| Class with `__init__` method that takes at least 1 argument | `ImageCatalog::__init__()` takes a directory `str` as parameter in `imagecatalog.py`
| Class with `__repr__` method | `ImageCatalog::__repr__()` in `imagecatalog.py` |
| Magic methods | `ImageCatalog::__len__()`, `ImageCatalog::__getitem__()` in `imagecatalog.py`


## Troubleshooting

if this error is displayed while running the app:

```shell
Traceback (most recent call last):
  File "/.../bu-ms-s2-tp/tkinter_test.py", line 8, in <module>
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

