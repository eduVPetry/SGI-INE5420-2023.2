from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QTableWidget, QTableWidgetItem

from model.window import Window


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
        self.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def add(self, graphical_object):
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(graphical_object.type))
        self.setItem(row_position, 1, QTableWidgetItem(graphical_object.name))
        self.graphical_objects.append(graphical_object)

    def removeCurrentRow(self):
        current_row = self.currentRow()
        if current_row >= 0:
            self.removeRow(current_row)
            object_type = self.graphical_objects[current_row].type
            del self.graphical_objects[current_row]
            return True, object_type
        return False, None
