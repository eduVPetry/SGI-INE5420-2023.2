from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QLabel


class Viewport(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.width = 1200
        self.height = 600
        self.x_min = 0
        self.y_min = 0
        self.x_max = self.width
        self.y_max = self.height
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color: black;")
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("red"), 4))

        display_file = self.window().display_file

        for graphical_object in display_file.graphical_objects:
            # Apply viewport transform
            transformed_coordinates = []
            for point in graphical_object.coordinates:
                new_point = self.viewport_transform(point)
                transformed_coordinates.append(new_point)

            # Draw graphical object according to its type
            if graphical_object.type == "Point":
                painter.drawPoint(transformed_coordinates[0])
            elif graphical_object.type == "Line":
                p1 = transformed_coordinates[0]
                p2 = transformed_coordinates[1]
                painter.drawLine(p1, p2)
            elif graphical_object.type == "Wireframe":
                for i in range(len(transformed_coordinates)-1):
                    p1 = transformed_coordinates[i]
                    p2 = transformed_coordinates[i+1]
                    painter.drawLine(p1, p2)
                p1 = transformed_coordinates[-1]
                p2 = transformed_coordinates[0]
                painter.drawLine(p1, p2)

    def viewport_transform(self, point: QPointF) -> QPointF:
        _window = self.window().display_file._window
        x_w, y_w = point.x(), point.y()
        x_v = (x_w - _window.x_min) / _window.width() * self.width
        y_v = (1 - (y_w - _window.y_min) / _window.height()) * self.height
        return QPointF(x_v, y_v)
