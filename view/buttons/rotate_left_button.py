from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton


class RotateLeftButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("rot. left")
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        ...
