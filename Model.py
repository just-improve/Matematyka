import re
from Zadaniam import Zadanie

class Model:
    def __init__(self):
        self.list_of_tasks = Zadanie.create_list_of_tasks(Zadanie.list_of_paths)


