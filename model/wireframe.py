from model.graphical_object import GraphicalObject


class Wireframe(GraphicalObject):
    def __init__(self, name, coordinates):
        super().__init__(name, "Wireframe", coordinates)
