from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton

from view.transformations_3d_dialog import Transformations3DDialog
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
        display_file = main_window.display_file
        current_row = display_file.currentRow()
        if current_row >= 0:
            graphical_object = display_file.graphical_objects[current_row]
            if graphical_object.type == "Wavefront OBJ" or \
                graphical_object.type == "Bézier Surface" or \
                graphical_object.type == "B-Spline Surface":
                dialog = Transformations3DDialog(graphical_object, self.window())
            else:
                dialog = TransformationsDialog(graphical_object, self.window())
            dialog.exec()
        else:
            main_window.debug_console.show_debug_message("There is no object currently selected.")
