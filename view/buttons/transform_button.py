from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton

from view.transformations_dialog import TransformationsDialog


class TransformButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Transform")
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        main_window = self.window()
        current_row = main_window.display_file.currentRow()
        if current_row >= 0:
            dialog = TransformationsDialog(current_row, self.window())
            dialog.exec()
        else:
            main_window.debug_console.show_debug_message("There is no object currently selected.")
