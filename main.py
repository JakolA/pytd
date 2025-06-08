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


def run():
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("Game")

    scene = QGraphicsScene()

    pixmap = QPixmap('media/map.png')
    map_item = QGraphicsPixmapItem(pixmap)
    map_item.setPos(0, 0)
    scene.addItem(map_item)

    exit_button = QPushButton("Exit")
    exit_button.clicked.connect(window.close)

    view = QGraphicsView(scene)

    layout = QVBoxLayout()
    layout.addWidget(view)
    layout.addWidget(exit_button)
    window.setLayout(layout)

    window.show()

    app.exec_()


if __name__ == '__main__':
    run()
