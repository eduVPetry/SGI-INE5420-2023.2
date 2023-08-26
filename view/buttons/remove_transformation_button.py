from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QPushButton


class RemoveTransformationButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Remove Transformation")
        self.setGeometry(QRect(430, 59, 201, 25))
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        transform_dialog = self.parent()
        current_row = transform_dialog.list_widget.currentRow()
        if current_row >= 0:
            transform_dialog.list_widget.takeItem(current_row)
            del transform_dialog.transformations[current_row]
