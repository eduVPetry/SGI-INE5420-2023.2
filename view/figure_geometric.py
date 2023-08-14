import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPolygon

# https://www.pythonguis.com/tutorials/bitmap-graphics/ link de onde peguei a class

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_line(x1, y1, x2, y2)
        self.draw_rect(a, b, c, d)
        self.draw_polygon(a1, b1, a2, b2, a3, b3)


    # Semi Reta
    def draw_line(self, x1, y1, x2, y2):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(x1, y1, x2, y2)
        painter.end()

    # Quadrado
    def draw_rect(self, a, b, c, d):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(Qt.blue)
        painter.drawRect(a, b, c, d)
        painter.end()

    # Poligono Triagulo
    def draw_polygon(self, a1, b1, a2, b2, a3, b3):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setPen(Qt.red)
        p2 = [QPoint(a1, b1), QPoint(a2, b2), QPoint(a3, b3)]
        painter.drawPolygon(QPolygon(p2))
        painter.end()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    x1, y1, x2, y2 = 10, 10, 100, 140
    a, b, c, d = 120, 10, 80, 80
    a1, b1 = 120, 110
    a2, b2 = 220, 110
    a3, b3 = 220, 190
    window = MainWindow()
    window.draw_line(x1, y1, x2, y2)
    window.draw_rect(a, b, c, d)
    window.draw_polygon(a1, b1, a2, b2, a3, b3)
    window.show()
    app.exec_()
