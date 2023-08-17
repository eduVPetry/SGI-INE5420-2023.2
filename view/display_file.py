from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from view.window import Window


class DisplayFile(QTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.graphical_objects = []
        self._window = Window(0, 0, 1200, 600)
        self.init_ui()

    def init_ui(self):
        self.setColumnCount(2)
        self.setHorizontalHeaderItem(0, QTableWidgetItem("Type"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))

    def add(self, graphical_object):
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(graphical_object.type))
        self.setItem(row_position, 1, QTableWidgetItem(graphical_object.name))
        self.graphical_objects.append(graphical_object)

        main_window = self.window()
        main_window.viewport.update()  # Trigger viewport.paintEvent
        debug_message = f"{graphical_object.type} has been added to the display file and drawn to the viewport."
        main_window.debug_console.show_debug_message(debug_message)

    def removeCurrentRow(self):
        main_window = self.window()
        current_row = self.currentRow()
        if current_row >= 0:
            self.removeRow(current_row)
            object_type = self.graphical_objects[current_row].type
            del self.graphical_objects[current_row]
            main_window.viewport.clear()
            main_window.viewport.update()  # Trigger viewport.paintEvent
            debug_message = f"{object_type} has been removed from the display file and erased from the viewport."
        else:
            debug_message = "There is no object currently selected."
        main_window.debug_console.show_debug_message(debug_message)

    def clear(self):
        self.clearContents()
        self.setRowCount(0)
        self.graphical_objects.clear()

        main_window = self.window()
        main_window.viewport.clear()
        main_window.debug_console.show_debug_message("Display file has been cleared and all objects were erased.")