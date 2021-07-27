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

from imgviewer.utils import PATH_DATA_ROOT_DIR
from imgviewer.views.image_utils import ImageAttributes

logger = logging.getLogger(__name__)

BACKGROUND_LOGO_IMAGE_PATH = PATH_DATA_ROOT_DIR / 'bg-logo.jpg'


class MainView(tk.Frame):
    """
    Main View/frame
    """
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.master = master
        self.statusbar = None

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
        return selected_dir

    def set_status_bar_text(self, str):
        self.statusbar.config(text=str)

    def render(self):
        self.master.title('Image Viewer')
        self.pack(fill=tk.BOTH, expand=1)
        path = BACKGROUND_LOGO_IMAGE_PATH
        img = Image.open(path)

        # this is a test for resizing
        # https://stackoverflow.com/a/24745969/918858

        maxsize = (800, 600)
        logger.info('resizing image...')
        img.thumbnail(maxsize, Image.ANTIALIAS)

        img_frame = tk.Frame(self, width=800, height=600)
        img_frame.pack(fill=tk.BOTH, expand=True)
        pimg = ImageTk.PhotoImage(img)
        img_attr = ImageAttributes(img)

        img_label = tk.Label(img_frame, image=pimg)
        img_label.image = pimg
        img_label.pack()

        exif_label = tk.Label(img_frame, text=img_attr.get_formatted_exif(),
                              justify=tk.LEFT)

        # place the EXIF relative to the image
        # https://stackoverflow.com/a/63625317/918858
        exif_label.place(in_=img_label, y=10, x=10)

        self.statusbar = tk.Label(self, text='Ready.', bd=1,
                                  relief=tk.SUNKEN, anchor=tk.W)
        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)

        rating = tk.Scale(self, from_=0, to=5, orient=tk.HORIZONTAL)
        rating.pack(side=tk.LEFT, padx=20, pady=20)
        next_button = tk.Button(self, text='Next Image')
        previous_button = tk.Button(self, text='Previous Image')

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
    root.geometry('800x700')

    # https://www.tutorialspoint.com/how-to-center-a-window-on-the-screen-in-tkinter
    root.eval('tk::PlaceWindow . center')
    root.mainloop()
