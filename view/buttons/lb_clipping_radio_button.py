from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QRadioButton

from model.clipping import liang_barsky_clipping


class LBClippingRadioButton(QRadioButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Liang-Barsky")
        self.toggled.connect(self.toggled_callback)

    @pyqtSlot(bool)
    def toggled_callback(self, checked):
        if checked:
            self.window().viewport.clipping_method = liang_barsky_clipping
