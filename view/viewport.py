from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QLabel

class Viewport(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.width = 1200
        self.height = 600
        self.init_ui()
    
    def init_ui(self):
        self.setFixedSize(self.width, self.height)
        self.clear()
        self.show()
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("red"), 4))

        display_file = self.window().display_file

        for graphical_object in display_file.graphical_objects:
            if graphical_object.type == "Point":
                painter.drawPoint(graphical_object)
            elif graphical_object.type == "Line":
                painter.drawLine(graphical_object)
            elif graphical_object.type == "Wireframe":
                for i in range(len(graphical_object.coordinates)-1):
                    p1 = graphical_object.coordinates[i]
                    p2 = graphical_object.coordinates[i+1]
                    painter.drawLine(p1, p2)
                p1 = graphical_object.coordinates[-1]
                p2 = graphical_object.coordinates[0]
                painter.drawLine(p1, p2)

    def clear(self):
        self.setStyleSheet("background-color: black;")
