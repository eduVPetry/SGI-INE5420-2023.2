from PyQt5.QtWidgets import QPushButton


class DownButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Down")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        ...
