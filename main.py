
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_Dialog
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)
        paint.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        for i in range(randint(1, 20)):
            a = randint(50, 100)
            paint.drawEllipse(randint(0, 300), randint(0, 225), a, a)
        paint.end()

    def draw(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())