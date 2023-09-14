from typing import List
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QLabel

from model.viewport import Viewport


class ViewportWidget(QLabel):

    def __init__(self, width, height, parent=None):
        super().__init__(parent)
        self._viewport = Viewport(width, height)
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(self._viewport.width, self._viewport.height)
        self.setStyleSheet("background-color: black;")
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        display_file = self.window().display_file

        for graphical_object in display_file.graphical_objects:
            # Set color and width for painting
            painter.setPen(QPen(QColor.fromRgb(graphical_object.color_rgb), 4))

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
