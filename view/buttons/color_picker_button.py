from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QColorDialog, QPushButton


class ColorPickerButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Select Color")
        self.setGeometry(QRect(271, 30, 100, 31))
        self.set_background_color(0xFFFFFF)
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        color_rgb = QColorDialog.getColor().rgb()
        self.set_background_color(color_rgb)
        self.parent().color_rgb = color_rgb

    def set_background_color(self, color_rgb: int):
        self.setStyleSheet(f"background-color: #{color_rgb:06x};")
