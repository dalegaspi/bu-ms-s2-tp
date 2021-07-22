# bu-ms-s2-tp
CS521 Term Project

## Requirements

- Tkinter

### Running the app

The app should be run as a python module.  The `PYTHONPATH` environment variable so the modules 

```shell
> cd imgviewer/
> export PYTHONPATH=`pwd`
> python -m imgviewer
```

### Running the unit tests

Running the unit tests using the standard `unittest` module is no different here.  The unit tests are located in the `/tests` sub-directory and it will discover and automatically run the tests and display the results

```shell
> cd tests/
> python -m unittest -v
```

### Install Tkinter libraries on MacOS

if this error is found:

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

