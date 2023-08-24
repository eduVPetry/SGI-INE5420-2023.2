from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QPushButton

from model.transformations import translation, rotation_around_center_of_world, natural_dilation


class AddTransformationButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Add Transformation")
        self.setGeometry(QRect(430, 28, 201, 25))
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        transform_dialog = self.parent()
        current_index = transform_dialog.tab_widget.currentIndex()
        if current_index == 0:  # Translation
            delta_x = float(transform_dialog.displacement_in_x_input.text())
            delta_y = float(transform_dialog.displacement_in_y_input.text())
            transformation_matrix = translation(delta_x, delta_y)
            transform_dialog.transformations.append(transformation_matrix)
            transform_dialog.list_widget.addItem(f"Translation: Dx={delta_x} Dy={delta_y}")
        elif current_index == 1:  # Rotation
            angle = float(transform_dialog.rotation_angle_input.text())
            transformation_matrix = rotation_around_center_of_world(angle)
            transform_dialog.transformations.append(transformation_matrix)
            transform_dialog.list_widget.addItem(f"Rotation: θ={angle}°")
        elif current_index == 2:  # Dilation
            scale_x = float(transform_dialog.scaling_in_x_input.text())
            scale_y = float(transform_dialog.scaling_in_y_input.text())
            center_x, center_y = transform_dialog.graphical_object.geometric_center()
            transformation_matrix = natural_dilation(scale_x, scale_y, center_x, center_y)
            transform_dialog.transformations.append(transformation_matrix)
            transform_dialog.list_widget.addItem(f"Dilation: Sx={scale_x} Sy={scale_y}")
