from PyQt5.QtWidgets import QPushButton


class RemoveButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Remove")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        main_window = self.parent().parent().parent()
        current_row = main_window.display_file.currentRow()
        if current_row >= 0:
            main_window.display_file.removeRow(current_row)
            del main_window.display_file.graphical_objects[current_row]
            main_window.debug_console.show_debug_message(f"Removed row of index {current_row} from the table.")
        else:
            main_window.debug_console.show_debug_message("There is no row selected to be removed from the table.")
