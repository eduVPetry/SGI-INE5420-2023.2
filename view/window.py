class Window:

    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

        self.PAN_FACTOR = 0.1
        self.ZOOM_FACTOR = 1.1

    def width(self):
        return self.x_max - self.x_min

    def height(self):
        return self.y_max - self.y_min

    def pan_up(self):
        delta_y = self.height() * self.PAN_FACTOR
        self.y_min += delta_y
        self.y_max += delta_y

    def pan_down(self):
        delta_y = self.height() * self.PAN_FACTOR
        self.y_min -= delta_y
        self.y_max -= delta_y

    def pan_left(self):
        delta_x = self.width() * self.PAN_FACTOR
        self.x_min -= delta_x
        self.x_max -= delta_x

    def pan_right(self):
        delta_x = self.width() * self.PAN_FACTOR
        self.x_min += delta_x
        self.x_max += delta_x

    def zoom_in(self):
        x_range = self.width() / 2
        y_range = self.height() / 2
        self.x_min += x_range * (1 - 1 / self.ZOOM_FACTOR)
        self.x_max -= x_range * (1 - 1 / self.ZOOM_FACTOR)
        self.y_min += y_range * (1 - 1 / self.ZOOM_FACTOR)
        self.y_max -= y_range * (1 - 1 / self.ZOOM_FACTOR)

    def zoom_out(self):
        x_range = self.width() / 2
        y_range = self.height() / 2
        self.x_min -= x_range * (self.ZOOM_FACTOR - 1)
        self.x_max += x_range * (self.ZOOM_FACTOR - 1)
        self.y_min -= y_range * (self.ZOOM_FACTOR - 1)
        self.y_max += y_range * (self.ZOOM_FACTOR - 1)
