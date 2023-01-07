import tkinter as tk
from tkinter import ttk
from tkinter import *

# from PIL import ImageTk, Image

from Zadaniam import Zadanie, Task


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Menu:')
        self.label.grid(row=1, column=0)

        # save button
        self.save_button = ttk.Button(self, text='Algebra')
        self.save_button.grid(row=1, column=3, padx=10)

        # show photos
        self.show_photos_btn = ttk.Button(self, text='Potegi', command=self.go_to_next_menu)
        self.show_photos_btn.grid(row=1, column=4, padx=10)

        # set the controller
        self.controller = None


    def go_to_next_menu(self):
        self.root = Tk()
        canvas = Canvas(self.root, width=700, height=300)
        canvas.pack()

        self.btn = Button(self.root, width=28, height=1, text="Zaczynamy - pokaż zadanie", command=self.show_task)
        self.btn.pack()

        mainloop()

    def show_task(self):
        if self.controller:
            self.controller.create_obj_photos()

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

