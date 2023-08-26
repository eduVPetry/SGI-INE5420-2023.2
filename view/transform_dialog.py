from typing import List
import numpy as np
from PyQt5.QtCore import Qt, QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QDialog, QDialogButtonBox, QFormLayout, QHBoxLayout,
    QLineEdit, QListWidget, QTabWidget, QVBoxLayout, QWidget
)

from model.transformations import compose
from view.buttons.add_transformation_button import AddTransformationButton
from view.buttons.remove_transformation_button import RemoveTransformationButton
from view.buttons.rotation_around_object_radio_button import RotationAroundObjectRadioButton
from view.buttons.rotation_around_point_radio_button import RotationAroundPointRadioButton
from view.buttons.rotation_around_world_radio_button import RotationAroundWorldRadioButton
from view.label import Label


class TransformDialog(QDialog):

    def __init__(self, object_index, parent=None):
        super().__init__(parent)
        self.graphical_object = self.parent().display_file.graphical_objects[object_index]
        self.transformations: List[np.array] = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Transformations")
        self.resize(640, 360)

        # Tabs
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(QRect(20, 20, 400, 328))

        self.translation_tab = QWidget(self.tab_widget)
        self.rotation_tab = QWidget(self.tab_widget)
        self.dilation_tab = QWidget(self.tab_widget)

        self.tab_widget.addTab(self.translation_tab, "Translation")
        self.tab_widget.addTab(self.rotation_tab, "Rotation")
        self.tab_widget.addTab(self.dilation_tab, "Dilation")

        # Widgets used for layouts
        self.displacement_input_widget = QWidget(self.translation_tab)
        self.rotation_options_widget = QWidget(self.rotation_tab)
        self.rotation_input_widget = QWidget(self.rotation_tab)
        self.scaling_input_widget = QWidget(self.dilation_tab)

        # Fonts for the labels
        font = QFont()
        font.setPointSize(12)

        font_bold = QFont()
        font_bold.setPointSize(12)
        font_bold.setBold(True)

        # Labels
        self.translation_label = Label("Translation", font_bold, self.translation_tab)
        self.displacement_in_x_label = Label("Displacement in x", font, self.displacement_input_widget)
        self.displacement_in_y_label = Label("Displacement in y", font, self.displacement_input_widget)
        self.options_label = Label("Options", font_bold, self.rotation_options_widget)
        self.rotation_type_label = Label("Rotation around the center of the world", font_bold, self.rotation_tab)
        self.rotation_angle_label = Label("Rotation angle (degrees)", font, self.rotation_input_widget)
        self.point_x_label = Label("x", font, self.rotation_input_widget)
        self.point_y_label = Label("y", font, self.rotation_input_widget)
        self.dilation_label = Label("Dilation", font_bold, self.dilation_tab)
        self.scaling_in_x_label = Label("Scaling in x", font, self.scaling_input_widget)
        self.scaling_in_y_label = Label("Scaling in y", font, self.scaling_input_widget)

        self.point_x_label.setVisible(False)
        self.point_y_label.setVisible(False)
        self.translation_label.setGeometry(QRect(30, 40, 111, 16))
        self.rotation_type_label.setGeometry(QRect(20, 160, 361, 21))
        self.dilation_label.setGeometry(QRect(30, 40, 81, 16))

        # Text inputs
        self.displacement_in_x_input = QLineEdit(self.displacement_input_widget)
        self.displacement_in_y_input = QLineEdit(self.displacement_input_widget)
        self.rotation_angle_input = QLineEdit(self.rotation_input_widget)
        self.point_x_input = QLineEdit(self.rotation_input_widget)
        self.point_y_input = QLineEdit(self.rotation_input_widget)
        self.scaling_in_x_input = QLineEdit(self.scaling_input_widget)
        self.scaling_in_y_input = QLineEdit(self.scaling_input_widget)

        self.point_x_input.setVisible(False)
        self.point_y_input.setVisible(False)

        # Radio Buttons
        self.radio_button = RotationAroundWorldRadioButton(self.rotation_options_widget)
        self.radio_button_2 = RotationAroundObjectRadioButton(self.rotation_options_widget)
        self.radio_button_3 = RotationAroundPointRadioButton(self.rotation_options_widget)

        # Push Buttons
        self.add_transformation_button = AddTransformationButton(self)
        self.remove_transformation_button = RemoveTransformationButton(self)

        # List widget
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(QRect(430, 90, 201, 211))

        # Layout
        self.displacement_input_widget.setGeometry(QRect(50, 80, 200, 58))
        self.verticalLayout_3 = QVBoxLayout(self.displacement_input_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.displacement_in_x_label)
        self.horizontalLayout_4.addWidget(self.displacement_in_x_input)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.addWidget(self.displacement_in_y_label)
        self.horizontalLayout_5.addWidget(self.displacement_in_y_input)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.rotation_options_widget.setGeometry(QRect(30, 30, 295, 102))
        self.verticalLayout = QVBoxLayout(self.rotation_options_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.options_label)
        self.verticalLayout.addWidget(self.radio_button)
        self.verticalLayout.addWidget(self.radio_button_2)
        self.verticalLayout.addWidget(self.radio_button_3)
        self.rotation_input_widget.setGeometry(QRect(50, 190, 256, 102))
        self.formLayout = QFormLayout(self.rotation_input_widget)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(3)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.rotation_angle_label)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.point_x_label)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.point_y_label)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.rotation_angle_input)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.point_x_input)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.point_y_input)
        self.scaling_input_widget.setGeometry(QRect(50, 80, 192, 58))
        self.verticalLayout_2 = QVBoxLayout(self.scaling_input_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.addWidget(self.scaling_in_x_label)
        self.horizontalLayout_2.addWidget(self.scaling_in_x_input)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.addWidget(self.scaling_in_y_label)
        self.horizontalLayout_3.addWidget(self.scaling_in_y_input)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # Ok and Cancel Buttons
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QRect(10, 310, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(self)

    def accept(self):
        transformation_matrix = compose(self.transformations)
        self.graphical_object.apply_transformation(transformation_matrix)
        self.parent().viewport.update()  # Trigger viewport.paintEvent

        super().accept()

    def reject(self):
        super().reject()
