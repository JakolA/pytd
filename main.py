from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem
)
from PyQt5.QtGui import QPixmap
from typing import List


class Game:
    def __init__(self, name):
        self.name = name

        app = QApplication([])
        wnd = self.init_window()
        wnd.show()
        app.exec_()

    def init_window(self):
        window = QWidget()
        window.setWindowTitle(self.name)

        window.resize(1430, 900)

        exit_button = QPushButton("Exit")
        exit_button.setFixedSize(30, 30)
        exit_button.clicked.connect(window.close)

        view = self.init_view()
        layout = self.layouting(view=view, objects=[exit_button])
        window.setLayout(layout)

        return window

    @staticmethod
    def init_view():
        scene = QGraphicsScene()

        pixmap = QPixmap('media/map.png')
        map_item = QGraphicsPixmapItem(pixmap)
        map_item.setPos(0, 0)

        barrack = QPixmap('media/barracks.png')
        barrack_item = QGraphicsPixmapItem(barrack)
        barrack_item.setPos(0, 119)

        scene.addItem(map_item)
        scene.addItem(barrack_item)

        view = QGraphicsView(scene)
        return view

    @staticmethod
    def layouting(view, objects: List):
        layout = QVBoxLayout()

        layout.addWidget(view)

        for obj in objects:
            layout.addWidget(obj)

        return layout


if __name__ == '__main__':
    Game('Game')
