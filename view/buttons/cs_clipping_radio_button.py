from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QRadioButton

from model.clipping import cohen_sutherland_clipping


class CSClippingRadioButton(QRadioButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Cohen-Sutherland")
        self.toggled.connect(self.toggled_callback)
        self.setChecked(True)

    @pyqtSlot(bool)
    def toggled_callback(self, checked):
        if checked:
            self.window().viewport.clipping_method = cohen_sutherland_clipping
