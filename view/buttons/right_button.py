from PyQt5.QtWidgets import QPushButton


class RightButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Right")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        main_window = self.window()
        main_window.display_file._window.pan_right()
        main_window.viewport.update()  # Trigger viewport.paintEvent
