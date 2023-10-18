from PyQt5.QtCore import pyqtSlot, Qt, QRect, QMetaObject
from PyQt5.QtGui import QDoubleValidator, QFont
from PyQt5.QtWidgets import (
    QDialog, QDialogButtonBox, QFileDialog, QLineEdit, QPushButton,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget
)
from model.bezier_curve import BezierCurve

from model.point import Point
from model.line import Line
from model.wavefront_obj import WavefrontOBJ
from model.wireframe import Wireframe
from view.buttons.color_picker_button import ColorPickerButton
from view.label import Label


class AddObjectDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Add Object")
        self.resize(470, 410)

        # Tabs
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setGeometry(QRect(30, 80, 401, 280))

        self.point_tab = QWidget(self.tab_widget)
        self.line_tab = QWidget(self.tab_widget)
        self.wireframe_tab = QWidget(self.tab_widget)
        self.wavefront_obj_tab = QWidget(self.tab_widget)
        self.bezier_curve_tab = QWidget(self.tab_widget)

        self.tab_widget.addTab(self.point_tab, "Point")
        self.tab_widget.addTab(self.line_tab, "Line")
        self.tab_widget.addTab(self.wireframe_tab, "Wireframe")
        self.tab_widget.addTab(self.wavefront_obj_tab, "Wavefront OBJ")
        self.tab_widget.addTab(self.bezier_curve_tab, "Bézier Curve")

        # Fonts for the labels
        font = QFont()
        font.setPointSize(12)

        font_bold = QFont()
        font_bold.setPointSize(12)
        font_bold.setBold(True)

        # Labels
        self.name_label = Label("Name", font_bold, self)
        self.point_label = Label("Point Coordinates", font_bold, self.point_tab)
        self.point_x_label = Label("x", font, self.point_tab)
        self.point_y_label = Label("y", font, self.point_tab)
        self.line_start_label = Label("Start Point Coordinates", font_bold, self.line_tab)
        self.line_end_label = Label("End Point Coordinates", font_bold, self.line_tab)
        self.line_x1_label = Label("x1", font, self.line_tab)
        self.line_y1_label = Label("y1", font, self.line_tab)
        self.line_x2_label = Label("x2", font, self.line_tab)
        self.line_y2_label = Label("y2", font, self.line_tab)

        self.name_label.setGeometry(QRect(30, 10, 57, 15))
        self.point_label.setGeometry(QRect(40, 30, 141, 16))
        self.point_x_label.setGeometry(QRect(60, 90, 16, 16))
        self.point_y_label.setGeometry(QRect(230, 90, 57, 15))
        self.line_start_label.setGeometry(QRect(30, 10, 180, 31))
        self.line_end_label.setGeometry(QRect(30, 140, 175, 16))
        self.line_x1_label.setGeometry(QRect(50, 80, 16, 16))
        self.line_y1_label.setGeometry(QRect(220, 80, 57, 15))
        self.line_x2_label.setGeometry(QRect(50, 200, 16, 16))
        self.line_y2_label.setGeometry(QRect(220, 200, 57, 15))

        # Text inputs
        self.name_input = QLineEdit(self)
        self.point_x_input = QLineEdit(self.point_tab)
        self.point_y_input = QLineEdit(self.point_tab)
        self.line_x1_input = QLineEdit(self.line_tab)
        self.line_y1_input = QLineEdit(self.line_tab)
        self.line_x2_input = QLineEdit(self.line_tab)
        self.line_y2_input = QLineEdit(self.line_tab)

        self.name_input.setGeometry(QRect(30, 30, 191, 31))
        self.point_x_input.setGeometry(QRect(80, 80, 111, 31))
        self.point_y_input.setGeometry(QRect(250, 80, 111, 31))
        self.line_x1_input.setGeometry(QRect(70, 70, 111, 31))
        self.line_y1_input.setGeometry(QRect(240, 70, 111, 31))
        self.line_x2_input.setGeometry(QRect(70, 190, 111, 31))
        self.line_y2_input.setGeometry(QRect(240, 190, 111, 31))

        # Input validator
        validator = QDoubleValidator()
        self.point_x_input.setValidator(validator)
        self.point_y_input.setValidator(validator)
        self.line_x1_input.setValidator(validator)
        self.line_y1_input.setValidator(validator)
        self.line_x2_input.setValidator(validator)
        self.line_y2_input.setValidator(validator)

        # Color picker
        self.color_rgb = 0xFFFFFF  # Default: white
        self.color_picker_button = ColorPickerButton(self)

        # Wireframe file selector
        self.wireframe_text_edit = QTextEdit(self.wireframe_tab)
        self.open_button = QPushButton("Open CSV File", self.wireframe_tab)
        self.open_button.clicked.connect(lambda: self.open_file("Wireframe", "wireframe", \
                                                                "CSV Files (*.csv)", self.wireframe_text_edit))

        layout = QVBoxLayout()
        layout.addWidget(self.wireframe_text_edit)
        layout.addWidget(self.open_button)
        self.wireframe_tab.setLayout(layout)

        # Wavefront OBJ file selector
        self.wavefront_obj_text_edit = QTextEdit(self.wavefront_obj_tab)
        self.open_button2 = QPushButton("Open Wavefront OBJ File", self.wavefront_obj_tab)
        self.open_button2.clicked.connect(lambda: self.open_file("Wavefront OBJ", "wavefront_obj", \
                                                                 "OBJ Files (*.obj)", self.wavefront_obj_text_edit))

        layout2 = QVBoxLayout()
        layout2.addWidget(self.wavefront_obj_text_edit)
        layout2.addWidget(self.open_button2)
        self.wavefront_obj_tab.setLayout(layout2)

        # Bézier Curve file selector
        self.bezier_curve_text_edit = QTextEdit(self.bezier_curve_tab)
        self.open_button3 = QPushButton("Open Bézier Curve File", self.bezier_curve_tab)
        self.open_button3.clicked.connect(lambda: self.open_file("Bézier Curve", "bezier_curve", \
                                                                 "CSV Files (*.csv)", self.bezier_curve_text_edit))

        layout3 = QVBoxLayout()
        layout3.addWidget(self.bezier_curve_text_edit)
        layout3.addWidget(self.open_button3)
        self.bezier_curve_tab.setLayout(layout3)

        # Ok and Cancel Buttons
        self.button_box = QDialogButtonBox(self)
        self.button_box.setGeometry(QRect(10, 370, 450, 32))
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.button_box.accepted.connect(self.ok_callback)
        self.button_box.rejected.connect(self.cancel_callback)

        QMetaObject.connectSlotsByName(self)

    def ok_callback(self):
        name = self.name_input.text()

        current_index = self.tab_widget.currentIndex()
        if current_index == 0:  # Point
            x = float(self.point_x_input.text())
            y = float(self.point_y_input.text())
            coordinates = [(x, y)]
            graphical_object = Point(name, self.color_rgb, coordinates)
        elif current_index == 1:  # Line
            x1 = float(self.line_x1_input.text())
            y1 = float(self.line_y1_input.text())
            x2 = float(self.line_x2_input.text())
            y2 = float(self.line_y2_input.text())
            coordinates = [(x1, y1), (x2, y2)]
            graphical_object = Line(name, self.color_rgb, coordinates)
        elif current_index == 2:  # Wireframe
            coordinates = []
            wireframe_data = self.wireframe_text_edit.toPlainText()
            lines = wireframe_data.strip().split("\n")
            for i in range(1, len(lines)):
                x, y = map(float, lines[i].split(","))
                coordinates.append((x, y))
            graphical_object = Wireframe(name, self.color_rgb, coordinates)
        elif current_index == 3:  # Wavefront OBJ
            coordinates = []
            faces = []
            wavefront_obj_data = self.wavefront_obj_text_edit.toPlainText()
            for line in wavefront_obj_data.split("\n"):
                if line.startswith("v "):
                    x, y, z = map(float, line.split()[1:4])
                    coordinates.append((x, y))
                elif line.startswith("f "):
                    face = tuple(map(int, line.split()[1:]))
                    faces.append(face)
            graphical_object = WavefrontOBJ(name, self.color_rgb, coordinates, faces)
        elif current_index == 4:  # Bézier curve
            control_points = []
            bezier_curve_data = self.bezier_curve_text_edit.toPlainText()
            lines = bezier_curve_data.strip().split("\n")
            for i in range(1, len(lines)):
                x, y = map(float, lines[i].split(","))
                control_points.append((x, y))
            graphical_object = BezierCurve(name, self.color_rgb, control_points)

        main_window = self.parent()
        main_window.display_file.add(graphical_object)
        main_window.viewport.update()  # Trigger viewport.paintEvent
        debug_message = f"{graphical_object.type} has been added to the display file and drawn to the viewport."
        main_window.debug_console.show_debug_message(debug_message)

        super().accept()

    def cancel_callback(self):
        super().reject()

    @pyqtSlot()
    def open_file(self, file_category, folder_name, file_type_extension, text_edit):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, f"Open {file_category} File", f"./{folder_name}",
                                                         f"{file_type_extension};;All Files (*)", options=options)

        if file_name:
            with open(file_name, "r") as file:
                content = file.read()
                text_edit.setPlainText(content)
