from graphical_object import GraphicalObject


class Point(GraphicalObject):
    def __init__(self, name, coordinates):
        super().__init__(name, "Point", coordinates)
