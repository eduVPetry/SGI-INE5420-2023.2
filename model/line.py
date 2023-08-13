from model.graphical_object import GraphicalObject


class Line(GraphicalObject):
    def __init__(self, name, coordinates):
        super().__init__(name, "Line", coordinates)
