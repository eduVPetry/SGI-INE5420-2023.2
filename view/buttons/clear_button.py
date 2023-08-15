from PyQt5.QtWidgets import QPushButton


class ClearButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Clear")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        main_window = self.parent().parent().parent()
        main_window.display_file.clearContents()
        main_window.display_file.setRowCount(0)
        main_window.display_file.graphical_objects.clear()
        main_window.debug_console.show_debug_message("Table has been cleared.")
