class Window:

    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

        self.X_MIN_NORM = self.Y_MIN_NORM = -1
        self.X_MAX_NORM = self.Y_MAX_NORM = 1

        self.x_pan = 0
        self.y_pan = 0
        self.viewup_angle = 0  # degrees

        self.PAN_FACTOR = 0.1
        self.ZOOM_FACTOR = 1.1
        self.ROTATION_ANGLE_ABSOLUTE = 10  # degrees

    def width(self):
        return self.x_max - self.x_min

    def height(self):
        return self.y_max - self.y_min

    def center(self):
        x_center = (self.x_min + self.x_max) / 2
        y_center = (self.y_min + self.y_max) / 2
        return x_center, y_center

    def pan_up(self):
        self.y_pan += self.PAN_FACTOR * self.height()

    def pan_down(self):
        self.y_pan -= self.PAN_FACTOR * self.height()

    def pan_left(self):
        self.x_pan -= self.PAN_FACTOR * self.width()

    def pan_right(self):
        self.x_pan += self.PAN_FACTOR * self.width()

    def zoom_in(self):
        half_width = self.width() / 2
        half_height = self.height() / 2
        self.x_min += half_width * (1 - 1 / self.ZOOM_FACTOR)
        self.x_max -= half_width * (1 - 1 / self.ZOOM_FACTOR)
        self.y_min += half_height * (1 - 1 / self.ZOOM_FACTOR)
        self.y_max -= half_height * (1 - 1 / self.ZOOM_FACTOR)

    def zoom_out(self):
        half_width = self.width() / 2
        half_height = self.height() / 2
        self.x_min -= half_width * (self.ZOOM_FACTOR - 1)
        self.x_max += half_width * (self.ZOOM_FACTOR - 1)
        self.y_min -= half_height * (self.ZOOM_FACTOR - 1)
        self.y_max += half_height * (self.ZOOM_FACTOR - 1)

    def rotate_left(self):
        self.viewup_angle -= self.ROTATION_ANGLE_ABSOLUTE

    def rotate_right(self):
        self.viewup_angle += self.ROTATION_ANGLE_ABSOLUTE
