from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QPixmap
from typing import Optional


class ClickablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap: 'QPixmap', game, obj_type: str):
        super().__init__(pixmap)
        self.game = game
        self.obj_type = obj_type

    def mousePressEvent(self, event: Optional['QGraphicsSceneMouseEvent']) -> None:
        self.view_selected_object(self.obj_type)
        print('barrack is selected')
        super().mousePressEvent(event)

    def view_selected_object(self, obj_type):
        self.game.selected_game_object = obj_type
