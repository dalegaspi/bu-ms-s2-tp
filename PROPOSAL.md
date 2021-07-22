# Term Project Proposal

### The Application

An Image (JPEG) viewer that will allow user view and rate the images in a specified folder.

### Description and Feature Set

The app will be an image (JPEG only) viewer that uses Tkinter to display a GUI, it will initially have a button to pop up a select dialog directory.  The app will then filter all the JPEG files (no directory recursion) and the GUI will display the first JPG image and will have a previous/next buttons to cycle through the images.  The app will try to extract EXIF information if it can and display alongside the image.  Once the last image has been reached using the next button, it will go back to the first image; conversely, if previous reaches the first image, it will go to the last image.

If the folder has no JPEG images, The UI will pop up a dialog to tell the user that the folder has no JPEG images.

It will have a slider to assign a rating (0 to 5, defaults to 0 meaning "no rating").  The GUI will have the option to "save ratings" which then generates a ratings data file (default file name _ratings.dat) in the same directory as the images; the file will be in CSV format.  Only the ones with rating (i.e., images with `rating > 0`) will be saved in the file.  

An example `_ratings.dat` content:

```csv
filename,rating
image1.jpg,3
image2.jpg,4
```

If the directory has the ratings data file already, it will be read and the images (matching by filename) that has ratings will default to that rating when displayed.  If, for whatever reason, the ratings file cannot be created, the user will be given a warning with the applicable error message.

It will prompt the user for confirmation when exiting the app (unless configured not to do so).

### Configuration

The app will have a configuration file and will be using a configuration file and will use the standard `configparser` module for reading the configuration (ini) file.  It will have the configuration for:

- initial window size
- ratings data filename
- confirm exit app

### Python Libraries to be Used

The following libraries will be used:

- Tkinter (for the GUI)
- Pillow (for the GUI, image render/display, EXIF extraction)
