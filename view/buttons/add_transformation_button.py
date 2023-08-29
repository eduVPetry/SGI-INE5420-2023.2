from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtWidgets import QPushButton

from model.transformations import (
    translation, rotation_around_center_of_world, rotation_around_center_of_object,
    rotation_around_arbitrary_point, natural_dilation
)


class AddTransformationButton(QPushButton):

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
            transformation_matrix = translation(delta_x, delta_y)
            list_item = f"Translation:\n    Dx={delta_x} Dy={delta_y}"

        elif current_index == 1:  # Rotation
            angle = float(dialog.rotation_angle_input.text())
            list_item = f"Rotation:\n    θ={angle}°"

            if dialog.radio_button.isChecked():
                transformation_matrix = rotation_around_center_of_world(angle)
            elif dialog.radio_button_2.isChecked():
                center_x, center_y = dialog.graphical_object.geometric_center()
                transformation_matrix = rotation_around_center_of_object(angle, center_x, center_y)
            elif dialog.radio_button_3.isChecked():
                x = float(dialog.point_x_input.text())
                y = float(dialog.point_y_input.text())
                transformation_matrix = rotation_around_arbitrary_point(angle, x, y)
                list_item += f" x={x} y={y}"

        elif current_index == 2:  # Dilation
            scale_x = float(dialog.scaling_in_x_input.text())
            scale_y = float(dialog.scaling_in_y_input.text())
            center_x, center_y = dialog.graphical_object.geometric_center()
            transformation_matrix = natural_dilation(scale_x, scale_y, center_x, center_y)
            list_item = f"Dilation:\n    Sx={scale_x} Sy={scale_y}"

        dialog.clear_input_widgets()
        dialog.list_widget.addItem(list_item)
        dialog.transformations.append(transformation_matrix)
