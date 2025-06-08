from PyQt5.QtWidgets import QGraphicsPixmapItem, QGraphicsSceneMouseEvent
from PyQt5.QtGui import QPixmap
from typing import Optional

from game_objects import view_selected_object


class ClickablePixmapItem(QGraphicsPixmapItem):
    def __init__(self, pixmap: 'QPixmap', obj_type: str):
        super().__init__(pixmap)
        self.obj_type = obj_type

    def mousePressEvent(self, event: Optional['QGraphicsSceneMouseEvent']) -> None:
        view_selected_object(self.obj_type)
        super().mousePressEvent(event)
