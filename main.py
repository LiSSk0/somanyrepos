import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(650, 270, 500, 420)
        uic.loadUi("UI.ui", self)
        self.setWindowTitle('circles are gods')
        self.setFixedSize(600, 600)

        self.doPaint = None

        self.btn.clicked.connect(self.spawnCircle)

    def spawnCircle(self):
        self.doPaint = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        if self.doPaint:
            qp.setPen(QColor(0, 0, 0))
            qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            radius = randint(10, 250)
            qp.drawEllipse(randint(0, 600), randint(0, 600), radius, radius)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())