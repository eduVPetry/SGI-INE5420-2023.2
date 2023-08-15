from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class DisplayFile(QTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.graphical_objects = []
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

        main_window = self.parent().parent().parent()
        debug_message = (
            f"{graphical_object.type} has been added to the table at index {row_position}.\n"
            f"Coordinates: {graphical_object.coordinates}."
        )
        main_window.debug_console.show_debug_message(debug_message)
