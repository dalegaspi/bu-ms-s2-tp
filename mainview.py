"""
Dexter Legaspi - dlegaspi@bu.edu
Class: CS 521 - Summer 2
Date: 07/22/2021
Term Project
Main view/window
"""
import logging
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image

from constants import PATH_DATA_ROOT_DIR, APP_CFG_WIN_DIMENSION, \
    APP_CFG_IMG_DIMENSION
from imageattributes import ImageAttributes

logger = logging.getLogger(__name__)

BACKGROUND_LOGO_IMAGE_PATH = PATH_DATA_ROOT_DIR / 'bg-logo2.jpg'
DOGE_IMAGE_PATH = PATH_DATA_ROOT_DIR / 'doge.jpg'


class MainView(tk.Frame):
    """
    Main View/frame
    """

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.master = master
        self.statusbar = None
        self.img_frame = None
        self.img_label = None
        self.exif_label = None
        self.render()
        self.render_menu()

    def render_menu(self):
        """
        renders the menu
        :return:
        """
        menu_bar = tk.Menu(self.master)
        main_menu = tk.Menu(menu_bar, tearoff=False)
        main_menu.add_command(label='Open...', command=self.menu_open_directory)
        main_menu.add_command(label='Quit', command=self.menu_command_quit)
        menu_bar.add_cascade(label='File', menu=main_menu)
        self.master.config(menu=menu_bar)

    def menu_command_quit(self):
        """
        quits application with confirmation
        :return:
        """
        # todo: processing of confirmation via config
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()

    def menu_open_directory(self):
        """
        open/select directory dialog
        :return:
        """
        selected_dir = filedialog.askdirectory(parent=self.master,
                                               initialdir='~',
                                               title='Select Images Directory')
        logger.info("open directory: %s", selected_dir)
        self.set_status_bar_text(f'Open directory: {selected_dir}')
        doge_img = Image.open(DOGE_IMAGE_PATH)
        self.set_img(doge_img)

        return selected_dir

    def set_status_bar_text(self, status_text):
        """
        sets the status bar text

        :param status_text:
        :return:
        """
        self.statusbar.config(text=status_text)

    def _init_img_widget(self):
        path = BACKGROUND_LOGO_IMAGE_PATH
        img = Image.open(path)

        # this is a test for resizing
        # https://stackoverflow.com/a/24745969/918858

        maxsize = (APP_CFG_IMG_DIMENSION[0], APP_CFG_IMG_DIMENSION[1])
        logger.info('resizing image...')
        img.thumbnail(maxsize, Image.ANTIALIAS)

        self.img_frame = tk.Frame(self,
                                  width=APP_CFG_WIN_DIMENSION[0],
                                  height=APP_CFG_WIN_DIMENSION[1])
        self.img_frame.pack(fill=tk.BOTH, expand=True)
        pimg = ImageTk.PhotoImage(img)
        img_attr = ImageAttributes(img)

        self.img_label = tk.Label(self.img_frame, image=pimg)
        self.img_label.image = pimg
        self.img_label.pack()

        self.exif_label = tk.Label(self.img_frame,
                                   text=img_attr.get_formatted_exif(),
                                   justify=tk.LEFT)

        # place the EXIF relative to the image
        # https://stackoverflow.com/a/63625317/918858
        self.exif_label.place(in_=self.img_label, y=10, x=10)

    def set_img(self, img):
        pimg = ImageTk.PhotoImage(img)
        img_attr = ImageAttributes(img)
        self.img_label.configure(image=pimg)
        self.img_label.image = pimg
        self.img_label.pack()

    def render(self):
        self.master.title('Image Viewer')
        self.pack(fill=tk.BOTH, expand=1)

        self._init_img_widget()


        self.statusbar = tk.Label(self, text='Ready.', bd=1,
                                  relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        rating = tk.Scale(self, from_=0, to=5, orient=tk.HORIZONTAL)
        rating.pack(side=tk.LEFT, padx=20, pady=20)
        next_button = tk.Button(self, text='Next Image')
        previous_button = tk.Button(self, text='Previous Image')

        # disable for now
        rating.set(3)
        # rating['state'] = 'disabled'
        # next_button['state'] = 'disabled'
        # previous_button['state'] = 'disabled'

        next_button.pack(side=tk.RIGHT, padx=2, pady=10)
        previous_button.pack(side=tk.RIGHT, padx=2, pady=10)


def render_main_view(controller):
    """
    render the main view

    :return:
    """
    root = tk.Tk()
    main_view = MainView(root, controller)

    # todo: get geometry from config
    root.geometry(f'{APP_CFG_WIN_DIMENSION[0]}x{APP_CFG_WIN_DIMENSION[1]}')

    # https://www.tutorialspoint.com/how-to-center-a-window-on-the-screen-in-tkinter
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
