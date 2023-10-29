from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QPushButton

from model.transformations import natural_dilation_3d, rotation_x, rotation_y, rotation_z, translation_3d


class AddTransformation3DButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Add Transformation")
        self.setGeometry(QRect(430, 28, 201, 25))
        self.clicked.connect(self.clicked_callback)

    @pyqtSlot()
    def clicked_callback(self):
        dialog = self.parent()
        current_index = dialog.tab_widget.currentIndex()

        if current_index == 0:  # Translation
            delta_x = float(dialog.displacement_in_x_input.text())
            delta_y = float(dialog.displacement_in_y_input.text())
            delta_z = float(dialog.displacement_in_z_input.text())
            transformation_matrix = translation_3d(delta_x, delta_y, delta_z)
            list_item = f"Translation:\n    Dx={delta_x} Dy={delta_y} Dz={delta_z}"

        elif current_index == 1:  # Rotation
            angle = float(dialog.rotation_angle_input.text())
            list_item = ""
            if dialog.rotation_x_radio_button.isChecked():
                transformation_matrix = rotation_x(angle)
                list_item += "Rotation around X axis:\n"
            elif dialog.rotation_y_radio_button.isChecked():
                transformation_matrix = rotation_y(angle)
                list_item += "Rotation around Y axis:\n"
            elif dialog.rotation_z_radio_button.isChecked():
                transformation_matrix = rotation_z(angle)
                list_item += "Rotation around Z axis:\n"
            list_item += f"    θ={angle}°"

        elif current_index == 2:  # Dilation
            scale_x = float(dialog.scaling_in_x_input.text())
            scale_y = float(dialog.scaling_in_y_input.text())
            scale_z = float(dialog.scaling_in_z_input.text())
            center_x, center_y, center_z = dialog.graphical_object.geometric_center()
            transformation_matrix = natural_dilation_3d(scale_x, scale_y, scale_z, center_x, center_y, center_z)
            list_item = f"Dilation:\n    Sx={scale_x} Sy={scale_y} Sz={scale_z}"

        dialog.clear_input_widgets()
        dialog.list_widget.addItem(list_item)
        dialog.transformations.append(transformation_matrix)
