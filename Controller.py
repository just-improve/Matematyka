import random

from Zadaniam import Zadanie


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    def create_obj_photos(self):
        random_task = random.choice(self.model.list_of_tasks)
        random_task.display_obj_image()


    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:

            # save the model
            self.model.email = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)
