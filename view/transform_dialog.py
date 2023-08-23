from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QPushButton, QRadioButton, QTabWidget, QVBoxLayout, QWidget
)

from view.label import Label


class TransformDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Transformations")
        self.resize(640, 348)

        # Tabs
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(QtCore.QRect(20, 20, 401, 281))

        self.translation_tab = QWidget(self.tab_widget)
        self.rotation_tab = QWidget(self.tab_widget)
        self.dilation_tab = QWidget(self.tab_widget)

        self.tab_widget.addTab(self.translation_tab, "Translation")
        self.tab_widget.addTab(self.rotation_tab, "Rotation")
        self.tab_widget.addTab(self.dilation_tab, "Dilation")

        # Widgets used for layouts
        self.displacement_widget = QWidget(self.translation_tab)
        self.rotation_options_widget = QWidget(self.rotation_tab)
        self.rotation_angle_widget = QWidget(self.rotation_tab)
        self.scaling_widget = QWidget(self.dilation_tab)

        # Fonts for the labels
        font = QtGui.QFont()
        font.setPointSize(12)

        font_bold = QtGui.QFont()
        font_bold.setPointSize(12)
        font_bold.setBold(True)

        # Labels
        self.translation_label = Label("Translation", font_bold, self.translation_tab)
        self.displacement_in_x_label = Label("Displacement in x", font, self.displacement_widget)
        self.displacement_in_y_label = Label("Displacement in y", font, self.displacement_widget)
        self.options_label = Label("Options", font_bold, self.rotation_options_widget)
        self.rotation_type_label = Label("Rotation around the center of the world", font_bold, self.rotation_tab)
        self.rotation_angle_label = Label("Rotation angle (degrees)", font, self.rotation_angle_widget)
        self.dilation_label = Label("Dilation", font_bold, self.dilation_tab)
        self.scaling_in_x_label = Label("Scaling in x", font, self.scaling_widget)
        self.scaling_in_y_label = Label("Scaling in y", font, self.scaling_widget)

        self.translation_label.setGeometry(QtCore.QRect(30, 40, 111, 16))
        self.rotation_type_label.setGeometry(QtCore.QRect(20, 160, 361, 21))
        self.dilation_label.setGeometry(QtCore.QRect(30, 40, 81, 16))

        # Text inputs
        self.lineEdit_4 = QLineEdit(self.displacement_widget)
        self.lineEdit_5 = QLineEdit(self.displacement_widget)
        self.lineEdit = QLineEdit(self.rotation_angle_widget)
        self.lineEdit_2 = QLineEdit(self.scaling_widget)
        self.lineEdit_3 = QLineEdit(self.scaling_widget)

        # Radio Buttons
        self.radio_button = QRadioButton(self.rotation_options_widget)
        self.radio_button_2 = QRadioButton(self.rotation_options_widget)
        self.radio_button_3 = QRadioButton(self.rotation_options_widget)

        self.radio_button.setChecked(True)
        self.radio_button.setText("Rotation around the center of the world")
        self.radio_button_2.setText("Rotation around the center of the object")
        self.radio_button_3.setText("Rotation around an arbitrary point")

        # Push Buttons
        self.add_button = QPushButton(self)
        self.add_button.setText("Add")
        self.add_button.setGeometry(QtCore.QRect(430, 28, 201, 25))

        self.remove_button = QPushButton(self)
        self.remove_button.setText("Remove")
        self.remove_button.setGeometry(QtCore.QRect(430, 59, 201, 25))

        # List widget
        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(QtCore.QRect(430, 90, 201, 211))

        # Layouting black magic
        self.displacement_widget.setGeometry(QtCore.QRect(50, 80, 200, 58))
        self.verticalLayout_3 = QVBoxLayout(self.displacement_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.displacement_in_x_label)
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.addWidget(self.displacement_in_y_label)
        self.horizontalLayout_5.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.rotation_options_widget.setGeometry(QtCore.QRect(30, 30, 295, 102))
        self.verticalLayout = QVBoxLayout(self.rotation_options_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.options_label)
        self.verticalLayout.addWidget(self.radio_button)
        self.verticalLayout.addWidget(self.radio_button_2)
        self.verticalLayout.addWidget(self.radio_button_3)
        self.rotation_angle_widget.setGeometry(QtCore.QRect(50, 190, 256, 25))
        self.horizontalLayout = QHBoxLayout(self.rotation_angle_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.addWidget(self.rotation_angle_label)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.scaling_widget.setGeometry(QtCore.QRect(50, 80, 192, 58))
        self.verticalLayout_2 = QVBoxLayout(self.scaling_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.addWidget(self.scaling_in_x_label)
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.addWidget(self.scaling_in_y_label)
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        # self.tab_widget.setCurrentIndex(1)

        # Ok and Cancel Buttons
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(10, 310, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QtCore.QMetaObject.connectSlotsByName(self)

    def accept(self):
        super().accept()

    def reject(self):
        super().reject()