from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QLabel

from model.viewport import Viewport


class ViewportWidget(QLabel):

    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self.width = width
        self.height = height

        self.HORIZONTAL_MARGIN = 10
        self.VERTICAL_MARGIN = 10
        x_min = self.HORIZONTAL_MARGIN
        y_min = self.VERTICAL_MARGIN
        x_max = width - self.HORIZONTAL_MARGIN
        y_max = height - self.VERTICAL_MARGIN
        self._viewport = Viewport(x_min, y_min, x_max, y_max)

        self.init_ui()

    def init_ui(self):
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color: black;")
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        # Draw margin
        painter.setPen(QPen(QColor("red"), 2))
        painter.drawLine(QPointF(self._viewport.x_min, self._viewport.y_min), QPointF(self._viewport.x_min, self._viewport.y_max))
        painter.drawLine(QPointF(self._viewport.x_min, self._viewport.y_max), QPointF(self._viewport.x_max, self._viewport.y_max))
        painter.drawLine(QPointF(self._viewport.x_max, self._viewport.y_max), QPointF(self._viewport.x_max, self._viewport.y_min))
        painter.drawLine(QPointF(self._viewport.x_max, self._viewport.y_min), QPointF(self._viewport.x_min, self._viewport.y_min))

        display_file = self.window().display_file

        for graphical_object in display_file.graphical_objects:
            # Set color and width for painting
            painter.setPen(QPen(QColor.fromRgb(graphical_object.color_rgb), 2))

            # Normalize world coordinates
            graphical_object.normalize(display_file._window)

            # Apply viewport transformation over normalized coordinates
            graphical_object.viewport_transform(self._viewport)

            # Draw graphical object according to its type
            if graphical_object.type == "Point":
                point = graphical_object.viewport_coordinates[0]
                painter.drawPoint(QPointF(*point))
            elif graphical_object.type == "Line":
                point1, point2 = graphical_object.viewport_coordinates
                painter.drawLine(QPointF(*point1), QPointF(*point2))
            elif graphical_object.type == "Wireframe":
                for i in range(len(graphical_object.viewport_coordinates)-1):
                    point1 = graphical_object.viewport_coordinates[i]
                    point2 = graphical_object.viewport_coordinates[i+1]
                    painter.drawLine(QPointF(*point1), QPointF(*point2))
                point1 = graphical_object.viewport_coordinates[-1]
                point2 = graphical_object.viewport_coordinates[0]
                painter.drawLine(QPointF(*point1), QPointF(*point2))
            elif graphical_object.type == "Wavefront OBJ":
                for face in graphical_object.faces:
                    for i in range(len(face)-1):
                        vertex_index1 = face[i]
                        vertex_index2 = face[i+1]
                        point1 = graphical_object.viewport_coordinates[vertex_index1-1]
                        point2 = graphical_object.viewport_coordinates[vertex_index2-1]
                        painter.drawLine(QPointF(*point1), QPointF(*point2))
                    vertex_index1 = face[-1]
                    vertex_index2 = face[0]
                    point1 = graphical_object.viewport_coordinates[vertex_index1-1]
                    point2 = graphical_object.viewport_coordinates[vertex_index2-1]
                    painter.drawLine(QPointF(*point1), QPointF(*point2))
