import tkinter as tk
from tkinter import *

class Zadanie:
    z1 = 'C://Users//xxx//PycharmProjects//Matematyka//Photos//potegi_1B.png'
    z2 = 'C://Users//xxx//PycharmProjects//Matematyka//Photos//potegi_2A.png'
    z3 = 'C://Users//xxx//PycharmProjects//Matematyka//Photos//potegi_3C.png'
    z4 = 'C://Users//xxx//PycharmProjects//Matematyka//Photos//potegi_4D.png'

    list_of_paths = [z1,z2,z3,z4]
    # list_of_tasks = []

    def __init__(self, path_dir):
        self.answer = 'a'
        self.path_dir = path_dir

    def display_obj_image(self):
        root = Tk()
        canvas = Canvas(root, width=600, height=700)
        canvas.pack()
        img = PhotoImage(file=self.path_dir, master=root)
        canvas.create_image(40, 80, anchor=NW, image=img)
        mainloop()

    @staticmethod
    def create_list_of_tasks(list_of_paths):
        list_of_tasks = []
        for x in list_of_paths:
            zadanie = Zadanie(x)
            list_of_tasks.append(zadanie)
        return list_of_tasks


class Task:
    def __init__(self):
        root = Tk()
        canvas = Canvas(root, width=600, height=700)
        canvas.pack()
        img = PhotoImage(file='C://Users//xxx//PycharmProjects//Matematyka//Photos//potegi_1.png')
        canvas.create_image(40, 80, anchor=NW, image=img)
        mainloop()
