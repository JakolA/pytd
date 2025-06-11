class GameObject:
    def on_selected(self):
        pass


class Barrack(GameObject):
    def on_selected(self):
        pass


class EnemyThrone(GameObject):
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.curr_hp = max_hp

    def on_selected(self):
        pass
