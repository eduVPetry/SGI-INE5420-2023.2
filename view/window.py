from .debug_console import DebugConsole
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

    def pan_up(self):
        self.y_min = self.y_min + 10
        self.y_max = self.y_max + self.y_min

    def pan_down(self):
        self.y_min = self.y_min - 10
        if self.y_min < 0:
            self.y_max = self.y_max + self.y_min
        else:
            self.y_max = self.y_max - self.y_min

    def pan_left(self):
        self.x_min = self.x_min - 10
        if self.x_min < 0:
            self.x_max = self.x_max + self.x_min
        else:
            self.x_max = self.x_max - self.x_min

    def pan_right(self):
        self.x_min = self.x_min + 10
        self.x_max = self.x_max + self.x_min

    def zoom_in(self):
        if self.check_max_zoom():
            message = "Maximum zoom reached!\n"
            DebugConsole().show_debug_message(message)
        else:
            self.x_max -= self.x_max * 0.1
            self.y_max -= self.y_max * 0.1
            self.x_min += self.x_max * 0.1
            self.y_min += self.y_max * 0.1

    def zoom_out(self):
        self.x_max += self.x_max * 0.1
        self.y_max += self.y_max * 0.1
        self.x_min -= self.x_max * 0.1
        self.y_min -= self.y_max * 0.1

    def get_size(self):
        size_x = self.x_max - self.x_min
        size_y = self.y_max - self.y_min
        return size_x, size_y

    def check_max_zoom(self):
        x, y = self.get_size()

        # if the window is too small max zoom reached
        if x < 10 or y < 10:
            return True

        # If its possible to zoom in more
        return False
