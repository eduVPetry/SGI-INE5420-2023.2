class Window:

    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def width(self):
        return self.x_max - self.x_min

    def height(self):
        return self.y_max - self.y_min

    def pan_up():
        ...

    def pan_down():
        ...

    def pan_left():
        ...

    def pan_right():
        ...

    def zoom_in(self):
        ...

    def zoom_out(self):
        ...
