from PyQt5.QtWidgets import QRadioButton


class RotationAroundPointRadioButton(QRadioButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setText("Rotation around an arbitrary point")
        self.toggled.connect(self.toggled_callback)

    def toggled_callback(self, checked):
        transform_dialog = self.window()

        if checked:
            transform_dialog.rotation_type_label.setText("Rotation around an arbitrary point")

        transform_dialog.point_x_label.setVisible(checked)
        transform_dialog.point_x_input.setVisible(checked)
        transform_dialog.point_y_label.setVisible(checked)
        transform_dialog.point_y_input.setVisible(checked)
