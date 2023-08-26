from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton


class ZoomInButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setIcon(QIcon("./view/buttons/icons/zoom-in.svg"))
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        main_window = self.window()
        main_window.display_file._window.zoom_in()
        main_window.viewport.update()  # Trigger viewport.paintEvent
