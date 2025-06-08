def view_selected_object(obj_type):
    if obj_type == 'barrack':
        print('Barrack is selected')


class GameObject:
    pass


class Barrack(GameObject):
    def on_selected(self):
        pass
