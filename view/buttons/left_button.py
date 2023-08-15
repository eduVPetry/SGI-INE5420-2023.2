from PyQt5.QtWidgets import QPushButton


class LeftButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Left")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        ...