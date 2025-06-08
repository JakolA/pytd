from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem,
    QLabel
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from typing import List

from qt5_extende import ClickablePixmapItem
from game_objects import Barrack


class Game(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.timer = QTimer()
        self.time_steps = 0
        self.wnd, self.layout = self.init_window()

        self.time_elapsed = QLabel(f"Time: {self.time_steps}")
        self.layout.addWidget(self.time_elapsed)

        self.btn_toggle = QPushButton("Pause")
        self.btn_toggle.clicked.connect(self.toggle_timer)
        self.btn_toggle.setFixedSize(60, 30)
        self.layout.addWidget(self.btn_toggle)

        self.timer.timeout.connect(self.update_game_status)
        self.timer.start(100)

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

        return window, layout

    @staticmethod
    def init_view():
        scene = QGraphicsScene()

        pixmap = QPixmap('media/map.png')
        map_item = QGraphicsPixmapItem(pixmap)
        map_item.setPos(0, 0)

        barrack = QPixmap('media/barracks.png')
        barrack_item = ClickablePixmapItem(barrack, obj_type='barrack')
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

    def toggle_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn_toggle.setText('Resume')
        else:
            self.timer.start(100)
            self.btn_toggle.setText('Pause')

    def update_game_status(self):
        self.time_steps += 1
        self.time_elapsed.setText(f'Time: {self.time_steps / 10}')
        self.wnd.update()


class GameWindow(Game, QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication([])
    g = Game('Game')
    g.wnd.show()
    app.exec_()
