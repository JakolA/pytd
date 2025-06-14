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

from qt5_extende import ClickablePixmapItem
from game_objects import GameObject


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.time_steps = 0
        self.selected_game_object = None
        self.scene = None
        self.view = None
        self.init_view()

        layout = QVBoxLayout()
        layout.addWidget(self.view)

        self.time_elapsed = QLabel(f"Time: {self.time_steps}")

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game_status)
        self.timer.start(80)

    def update_game_status(self):
        self.time_steps += 1
        self.time_elapsed.setText(f'Time: {self.time_steps / 10}')
        self.show_properties()
        self.update()

    def handle_events(self):
        pass

    def init_view(self):
        self.scene = QGraphicsScene()

        pixmap = QPixmap('media/map.png')
        map_item = QGraphicsPixmapItem(pixmap)
        map_item.setPos(0, 0)

        barrack = QPixmap('media/barracks.png')
        barrack_item = ClickablePixmapItem(barrack, game=self, obj_type='barrack')
        barrack_item.setPos(0, 119)

        self.scene.addItem(map_item)
        self.scene.addItem(barrack_item)

        self.view = QGraphicsView(self.scene)

    def show_properties(self):
        if self.selected_game_object == 'barrack':
            selected_zone_view = QPixmap('media/barrack_selected.png')
            barrack_selected = QGraphicsPixmapItem(selected_zone_view)
            barrack_selected.setPos(0, 605)
            self.scene.addItem(barrack_selected)
            self.view = QGraphicsView(self.scene)


class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.game_widget = Game()
        self.selected_game_object = None

        exit_button = QPushButton('Exit')
        exit_button.clicked.connect(self.close)

        self.pause_button = QPushButton('Pause')
        self.pause_button.clicked.connect(self.toggle_timer)

        layout.addWidget(self.game_widget)
        layout.addWidget(exit_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.game_widget.time_elapsed)
        layout.addWidget(self.game_widget.view)

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
