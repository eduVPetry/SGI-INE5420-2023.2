from math import cos, sin, radians

class Window:

    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.viewup_angle = 0  # degrees

        self.PAN_FACTOR = 0.1
        self.ZOOM_FACTOR = 1.1
        self.ROTATION_ANGLE_ABSOLUTE = 30  # degrees

    def width(self):
        return self.x_max - self.x_min

    def height(self):
        return self.y_max - self.y_min

    def center(self):
        x_center = (self.x_min + self.x_max) / 2
        y_center = (self.y_min + self.y_max) / 2
        return x_center, y_center

    def pan_up(self):
        d = self.PAN_FACTOR * self.height()
        dy = d * cos(self.viewup_angle)
        self.y_min += dy
        self.y_max += dy

    def pan_down(self):
        d = self.PAN_FACTOR * self.height()
        #dx = d * sin(self.viewup_angle)
        dy = d * cos(self.viewup_angle)
        self.y_min -= dy
        self.y_max -= dy

    def pan_left(self):
        d = self.PAN_FACTOR * self.width()
        dx = d * sin(self.viewup_angle)
        self.x_min -= dx
        self.x_max -= dx

    def pan_right(self):
        d = self.PAN_FACTOR * self.width()
        dx = d * sin(self.viewup_angle)
        self.x_min += dx
        self.x_max += dx

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
