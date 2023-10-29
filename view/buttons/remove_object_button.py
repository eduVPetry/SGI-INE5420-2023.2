from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton


class RemoveObjectButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Remove")
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        main_window = self.window()
        removed, object_type = self.window().display_file.removeCurrentRow()
        if removed:
            main_window.viewport.update()  # Trigger viewport.paintEvent
            debug_message = f"{object_type} has been removed from the display file and erased from the viewport."
        else:
            debug_message = "There is no object currently selected."
        main_window.debug_console.show_debug_message(debug_message)
