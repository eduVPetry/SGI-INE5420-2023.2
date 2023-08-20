from PyQt5 import QtCore, QtGui, QtWidgets

from model.point import Point
from model.line import Line
from model.wireframe import Wireframe
from view.label import Label


class InputDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Add Object")
        self.resize(640, 480)

        # Tabs
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(QtCore.QRect(30, 80, 571, 331))

        self.point_tab = QtWidgets.QWidget()
        self.line_tab = QtWidgets.QWidget()
        self.wireframe_tab = QtWidgets.QWidget()

        self.tab_widget.addTab(self.point_tab, "Point")
        self.tab_widget.addTab(self.line_tab, "Line")
        self.tab_widget.addTab(self.wireframe_tab, "Wireframe")

        # Fonts for the labels
        font = QtGui.QFont()
        font.setPointSize(12)

        font_bold = QtGui.QFont()
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

        self.name_label.setGeometry(QtCore.QRect(30, 10, 57, 15))
        self.point_label.setGeometry(QtCore.QRect(40, 30, 141, 16))
        self.point_x_label.setGeometry(QtCore.QRect(60, 90, 16, 16))
        self.point_y_label.setGeometry(QtCore.QRect(230, 90, 57, 15))
        self.line_start_label.setGeometry(QtCore.QRect(30, 10, 180, 31))
        self.line_end_label.setGeometry(QtCore.QRect(30, 140, 175, 16))
        self.line_x1_label.setGeometry(QtCore.QRect(50, 80, 16, 16))
        self.line_y1_label.setGeometry(QtCore.QRect(220, 80, 57, 15))
        self.line_x2_label.setGeometry(QtCore.QRect(50, 200, 16, 16))
        self.line_y2_label.setGeometry(QtCore.QRect(220, 200, 57, 15))

        # Text inputs
        self.name_input = QtWidgets.QLineEdit(self)
        self.point_x_input = QtWidgets.QLineEdit(self.point_tab)
        self.point_y_input = QtWidgets.QLineEdit(self.point_tab)
        self.line_x1_input = QtWidgets.QLineEdit(self.line_tab)
        self.line_y1_input = QtWidgets.QLineEdit(self.line_tab)
        self.line_x2_input = QtWidgets.QLineEdit(self.line_tab)
        self.line_y2_input = QtWidgets.QLineEdit(self.line_tab)

        self.name_input.setGeometry(QtCore.QRect(30, 30, 191, 31))
        self.point_x_input.setGeometry(QtCore.QRect(80, 80, 111, 31))
        self.point_y_input.setGeometry(QtCore.QRect(250, 80, 111, 31))
        self.line_x1_input.setGeometry(QtCore.QRect(70, 70, 111, 31))
        self.line_y1_input.setGeometry(QtCore.QRect(240, 70, 111, 31))
        self.line_x2_input.setGeometry(QtCore.QRect(70, 190, 111, 31))
        self.line_y2_input.setGeometry(QtCore.QRect(240, 190, 111, 31))

        # Ok and Cancel Buttons
        self.button_box = QtWidgets.QDialogButtonBox(self)
        self.button_box.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.accepted.connect(self.ok_callback)
        self.button_box.rejected.connect(self.cancel_callback)

        QtCore.QMetaObject.connectSlotsByName(self)

    def ok_callback(self):
        name = self.name_input.text()

        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            x = float(self.point_x_input.text())
            y = float(self.point_y_input.text())
            coordinates = [QtCore.QPointF(x, y)]
            graphical_object = Point(name, coordinates)
        elif current_index == 1:
            x1 = float(self.line_x1_input.text())
            y1 = float(self.line_y1_input.text())
            x2 = float(self.line_x2_input.text())
            y2 = float(self.line_y2_input.text())
            coordinates = [QtCore.QPointF(x1, y1), QtCore.QPointF(x2, y2)]
            graphical_object = Line(name, coordinates)
        elif current_index == 2:
            # To do: develop wireframe ...
            coordinates = []
            graphical_object = Wireframe(name, coordinates)

        main_window = self.parent()
        main_window.display_file.add(graphical_object)
        main_window.viewport.update()  # Trigger viewport.paintEvent
        debug_message = f"{graphical_object.type} has been added to the display file and drawn to the viewport."
        main_window.debug_console.show_debug_message(debug_message)

        super().accept()

    def cancel_callback(self):
        super().reject()
