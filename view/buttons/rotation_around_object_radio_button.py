from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QRadioButton


class RotationAroundObjectRadioButton(QRadioButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Rotation around the center of the object")
        self.toggled.connect(self.toggled_callback)

    @pyqtSlot(bool)
    def toggled_callback(self, checked):
        transform_dialog = self.window()

        if checked:
            transform_dialog.rotation_type_label.setText("Rotation around the center of the object")
