import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main_prog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('main.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        randomX = random.randint(20, 300)
        print(randomX)
        X1 = 100
        randomL = random.randint(20, 100)
        Y = randomX + randomL
        print(Y)
        Y1 = X1 + randomL
        qp.drawEllipse(randomX, X1, Y, Y1)
        qp.setBrush(QColor(255, 255, 0))
        randomX = random.randint(20, 300)
        randomL = random.randint(20, 100)
        Y = randomX + randomL
        Y1 = X1 + randomL
        qp.drawEllipse(randomX, X1, Y, Y1)
        qp.setBrush(QColor(255, 255, 0))
        randomX = random.randint(20, 300)
        randomL = random.randint(20, 100)
        Y = randomX + randomL
        Y1 = X1 + randomL
        qp.drawEllipse(randomX, X1, Y, Y1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_prog()
    ex.show()
    sys.exit(app.exec())