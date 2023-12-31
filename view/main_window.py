from PyQt5.QtCore import QMetaObject, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget

from view.buttons.add_object_button import AddObjectButton
from view.buttons.cs_clipping_radio_button import CSClippingRadioButton
from view.buttons.lb_clipping_radio_button import LBClippingRadioButton
from view.buttons.transform_button import TransformButton
from view.buttons.down_button import DownButton
from view.buttons.left_button import LeftButton
from view.buttons.remove_object_button import RemoveObjectButton
from view.buttons.right_button import RightButton
from view.buttons.rotate_left_button import RotateLeftButton
from view.buttons.rotate_right_button import RotateRightButton
from view.buttons.up_button import UpButton
from view.buttons.zoom_in_button import ZoomInButton
from view.buttons.zoom_out_button import ZoomOutButton

from view.debug_console import DebugConsole
from view.label import Label
from view.display_file import DisplayFile
from view.viewport_widget import ViewportWidget


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Interactive Graphics System")
        self.resize(1600, 800)
        self.centralWidget = QWidget(self)

        # Widget for the layout in the left side of the UI
        self.left_widget = QWidget(self.centralWidget)
        self.left_widget.setGeometry(QRect(10, 10, 256, 431))

        # Widget for the layout in the right side of the UI
        self.right_widget = QWidget(self.centralWidget)
        self.right_widget.setGeometry(QRect(321, 10, 661, 571))

        # Viewport
        self.viewport = ViewportWidget(1200, 600, self.right_widget)

        # Display file table (type, name)
        self.display_file = DisplayFile(self.left_widget)

        # Text console for debugging
        self.debug_console = DebugConsole(self.right_widget)

        # Font for the labels
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)

        # Labels
        self.table_label = Label("Display File", font, self.left_widget)
        self.control_label = Label("Window Control", font, self.left_widget)
        self.clipping_label = Label("Clipping", font, self.left_widget)
        self.viewport_label = Label("Viewport", font, self.right_widget)

        # Buttons
        self.add_object_button = AddObjectButton(self.left_widget)
        self.remove_object_button = RemoveObjectButton(self.left_widget)
        self.transform_button = TransformButton(self.left_widget)
        self.zoom_out_button = ZoomOutButton(self.left_widget)
        self.up_button = UpButton(self.left_widget)
        self.zoom_in_button = ZoomInButton(self.left_widget)
        self.left_button = LeftButton(self.left_widget)
        self.right_button = RightButton(self.left_widget)
        self.rotate_left_button = RotateLeftButton(self.left_widget)
        self.down_button = DownButton(self.left_widget)
        self.rotate_right_button = RotateRightButton(self.left_widget)
        self.cs_clipping_radio_button = CSClippingRadioButton(self.left_widget)
        self.lb_clipping_radio_button = LBClippingRadioButton(self.left_widget)

        # Layout in the left side of the UI
        self.vertical_layout = QVBoxLayout(self.left_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.addWidget(self.table_label)
        self.vertical_layout.addWidget(self.display_file)
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.add_object_button)
        self.horizontal_layout.addWidget(self.remove_object_button)
        self.horizontal_layout.addWidget(self.transform_button)
        self.vertical_layout.addLayout(self.horizontal_layout)
        self.vertical_layout.addWidget(self.control_label)
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.zoom_out_button, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.up_button, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.zoom_in_button, 0, 2, 1, 1)
        self.grid_layout.addWidget(self.left_button, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.right_button, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.rotate_left_button, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.down_button, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.rotate_right_button, 2, 2, 1, 1)
        self.vertical_layout.addLayout(self.grid_layout)
        self.vertical_layout.addWidget(self.clipping_label)
        self.vertical_layout_2 = QVBoxLayout()
        self.vertical_layout_2.addWidget(self.cs_clipping_radio_button)
        self.vertical_layout_2.addWidget(self.lb_clipping_radio_button)
        self.vertical_layout.addLayout(self.vertical_layout_2)

        # Layout in the right side of the UI
        self.vertical_layout_2 = QVBoxLayout(self.right_widget)
        self.vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_2.addWidget(self.viewport_label)
        self.vertical_layout_2.addWidget(self.viewport)
        self.vertical_layout_2.addWidget(self.debug_console)

        # Top-level layout
        self.horizontal_layout_2 = QHBoxLayout(self.centralWidget)
        self.horizontal_layout_2.addWidget(self.left_widget)
        self.horizontal_layout_2.addWidget(self.right_widget)

        self.setCentralWidget(self.centralWidget)
        QMetaObject.connectSlotsByName(self)
