from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem,
    QLabel
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt
from typing import List, Optional

from qt5_extende import ClickablePixmapItem
from game_objects import GameObject


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.time_steps = 0
        self.selected_game_object = None
        # self.wnd, self.layout = self.init_window()

        self.time_elapsed = QLabel(f"Time: {self.time_steps}")
        view = self.init_view()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game_status)
        self.timer.start(80)

    def init_window(self):
        window = QWidget()
        window.setWindowTitle(self.name)

        window.resize(1430, 900)

        #layout = self.layouting(view=view, objects=[exit_button])
        #window.setLayout(layout)

        return window

    def init_view(self):
        scene = QGraphicsScene()

        pixmap = QPixmap('media/map.png')
        map_item = QGraphicsPixmapItem(pixmap)
        map_item.setPos(0, 0)

        barrack = QPixmap('media/barracks.png')
        barrack_item = ClickablePixmapItem(barrack, game=self, obj_type='barrack')
        barrack_item.setPos(0, 119)

        selected_game_object = self.selected_game_object
        if selected_game_object is not None:
            selected_zone_view = QPixmap('media/barrack_selected.png')
            barrack_selected = QGraphicsPixmapItem(selected_zone_view)
            barrack_selected.setPos(0, 519)
            scene.addItem(barrack_selected)

        scene.addItem(map_item)
        scene.addItem(barrack_item)

        view = QGraphicsView(scene)
        return view

    def update_game_status(self):
        self.time_steps += 1
        self.time_elapsed.setText(f'Time: {self.time_steps / 10}')
        self.update()

    def handle_events(self):
        pass


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.game_widget = Game()

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)

        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.toggle_timer)

        layout.addWidget(self.game_widget)
        layout.addWidget(exit_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.game_widget.time_elapsed)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle('GameWindow')
        self.setFixedSize(1430, 900)

    def toggle_timer(self):
        timer = self.game_widget.timer
        if timer.isActive():
            timer.stop()
            self.pause_button.setText('Resume')
        else:
            timer.start()
            self.pause_button.setText('Pause')
