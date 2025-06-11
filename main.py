from PyQt5.QtWidgets import QApplication

from game import GameWindow


if __name__ == '__main__':
    app = QApplication([])
    window = GameWindow()
    window.show()
    app.exec_()
