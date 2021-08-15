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
from PIL import ImageTk, Image as PILImage

import appglobals
from appcontroller import AppController
from appstate import AppState
from image import Image
from imageattributes import ImageAttributes
from imagecatalog import ImageCatalog

logger = logging.getLogger(__name__)

BACKGROUND_LOGO_IMAGE_PATH = appglobals.path_data_root_door / 'bg-logo2.jpg'
DOGE_IMAGE_PATH = appglobals.path_data_root_door / 'doge.jpg'


class MainView(tk.Frame):
    """
    Main View/frame
    """

    def __init__(self, master, controller: AppController):
        """
        Constructor

        :param master:
        :param controller:
        """
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.master = master
        self.statusbar = None
        self.img_frame = None
        self.img_label = None
        self.exif_label = None
        self.exif_label_text = tk.StringVar()
        self.render()
        self.render_menu()

    def render_menu(self):
        """
        Render menu

        :return:
        """
        menu_bar = tk.Menu(self.master)
        main_menu = tk.Menu(menu_bar, tearoff=False)
        main_menu.add_command(label='Open...',
                              command=self.menu_open_directory)
        main_menu.add_command(label='Save Ratings',
                              command=self.menu_save_ratings)
        main_menu.add_command(label='Quit',
                              command=self.menu_command_quit)
        menu_bar.add_cascade(label='File',
                             menu=main_menu)
        self.master.config(menu=menu_bar)

    def menu_save_ratings(self):
        """
        save ratings

        :return:
        """
        logger.debug('save ratings...')
        pass

    def menu_command_quit(self):
        """
        Quit app

        :return:
        """

        logger.debug('quitting...')
        if appglobals.app_config_confirm_on_exit:
            logger.info('quit confirmation enabled')
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.master.destroy()
        else:
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
        catalog = ImageCatalog(directory=selected_dir)
        new_state = AppState(catalog)
        self.controller.set_state(new_state)

        #doge_img = Image.open(DOGE_IMAGE_PATH)
        #self.set_img(doge_img)

        initial_img = self.controller.get_state().get_image_at_current_index()
        if initial_img is not None:
            self.set_img(initial_img)

        return selected_dir

    def set_status_bar_text(self, status_text):
        """
        sets the status bar text

        :param status_text:
        :return:
        """
        self.statusbar.config(text=status_text)

    def __init_img_widget(self):
        """
        Image widget init

        :return:
        """
        path = BACKGROUND_LOGO_IMAGE_PATH
        img = PILImage.open(path)

        # this is a test for resizing
        # https://stackoverflow.com/a/24745969/918858

        maxsize = (appglobals.app_config_img_dimension[0],
                   appglobals.app_config_img_dimension[1])
        logger.info('resizing image...')
        img.thumbnail(maxsize, PILImage.ANTIALIAS)

        self.img_frame = tk.Frame(self,
                                  width=appglobals.app_config_win_dimension[0],
                                  height=appglobals.app_config_win_dimension[1])

        self.img_frame.pack(fill=tk.BOTH, expand=True)
        pimg = ImageTk.PhotoImage(img)
        img_attr = ImageAttributes(img)

        self.img_label = tk.Label(self.img_frame, image=pimg)
        self.img_label.image = pimg
        self.img_label.pack()

        self.exif_label_text.set(img_attr.get_formatted_exif())
        self.exif_label = tk.Label(self.img_frame,
                                   textvariable=self.exif_label_text,
                                   justify=tk.LEFT)

        # place the EXIF relative to the image
        # https://stackoverflow.com/a/63625317/918858
        self.exif_label.place(in_=self.img_label, y=10, x=10)

    def set_img(self, img: Image):
        """
        Set the image in the Main View

        :param img:
        :return:
        """
        raw_img = img.get_image_object()
        maxsize = (appglobals.app_config_img_dimension[0],
                   appglobals.app_config_img_dimension[1])
        logger.info('resizing image...')
        raw_img.thumbnail(maxsize, PILImage.ANTIALIAS)

        pimg = ImageTk.PhotoImage(raw_img)
        img_attr = img.get_attributes()
        self.exif_label_text.set(img_attr.get_formatted_exif())
        self.img_label.configure(image=pimg)
        self.img_label.image = pimg
        self.img_label.pack()

    def render(self):
        """
        Render UI

        :return:
        """
        self.master.title('Image Viewer')
        self.pack(fill=tk.BOTH, expand=1)

        self.__init_img_widget()

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

    root.geometry('{}x{}'
                  .format(appglobals.app_config_win_dimension[0],
                          appglobals.app_config_win_dimension[1]))

    # https://www.tutorialspoint.com/how-to-center-a-window-on-the-screen-in-tkinter
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
