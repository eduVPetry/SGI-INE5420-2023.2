class Viewport:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x_min = 0
        self.y_min = 0
        self.x_max = self.width
        self.y_max = self.height
