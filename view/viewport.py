from PyQt5.QtWidgets import QGraphicsView

class Viewport(QGraphicsView):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.width = 1200
        self.height = 600
        self.init_ui()
    
    def init_ui(self):
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color: black;")
