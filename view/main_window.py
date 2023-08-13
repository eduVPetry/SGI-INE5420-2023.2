from PyQt5 import QtCore, QtGui, QtWidgets

from view.input_dialog import InputDialog


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("mainWindow")
        self.setWindowTitle("Sistema Gráfico Interativo")
        self.resize(1000, 600)

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        # Font for the labels
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)

        # Widget for the layout in the left side of the UI
        self.left_widget = QtWidgets.QWidget(self.centralWidget)
        self.left_widget.setGeometry(QtCore.QRect(11, 10, 256, 431))
        self.left_widget.setObjectName("widgetLeft")

        # Vertical layout in the left side of the UI
        self.vertical_layout = QtWidgets.QVBoxLayout(self.left_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("verticalLayout")

        # Objects table label
        self.object_table_label = QtWidgets.QLabel(self.left_widget)
        self.object_table_label.setFont(font)
        self.object_table_label.setScaledContents(False)
        self.object_table_label.setObjectName("objTableLabel")
        self.object_table_label.setText("Objects")

        self.vertical_layout.addWidget(self.object_table_label)

        # Objects table (type, name)
        self.table_widget = QtWidgets.QTableWidget(self.left_widget)
        self.table_widget.setEnabled(True)
        self.table_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_widget.setDragEnabled(True)
        self.table_widget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.table_widget.setObjectName("tableWidget")
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(0)
    
        item = QtWidgets.QTableWidgetItem()
        item.setText("Type")
        self.table_widget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Name")
        self.table_widget.setHorizontalHeaderItem(1, item)

        self.table_widget.horizontalHeader().setCascadingSectionResizes(True)

        self.vertical_layout.addWidget(self.table_widget)

        # Add, remove and clear buttons in a horizontal layout
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontalLayout")
        
        self.add_button = QtWidgets.QPushButton(self.left_widget)
        self.add_button.setObjectName("addButton")
        self.add_button.setText("Add")
        self.add_button.clicked.connect(self.add_button_clicked)
        self.horizontal_layout.addWidget(self.add_button)

        self.remove_button = QtWidgets.QPushButton(self.left_widget)
        self.remove_button.setObjectName("removeButton")
        self.remove_button.setText("Remove")
        self.remove_button.clicked.connect(self.remove_button_clicked)
        self.horizontal_layout.addWidget(self.remove_button)

        self.clear_button = QtWidgets.QPushButton(self.left_widget)
        self.clear_button.setObjectName("clearButton")
        self.clear_button.setText("Clear")
        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.horizontal_layout.addWidget(self.clear_button)

        self.vertical_layout.addLayout(self.horizontal_layout)

        # Espaço entre os layouts
        self.vertical_layout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed))

        # Control label
        self.control_label = QtWidgets.QLabel(self.left_widget)
        self.control_label.setFont(font)
        self.control_label.setObjectName("controlLabel")
        self.control_label.setText("Control")

        self.vertical_layout.addWidget(self.control_label)

        # Window control buttons in a grid layout:
        #   Zoom in,   up, zoom out
        #      left,     , right
        # rot. left, down, rot. right

        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setObjectName("gridLayout")
        
        self.zoom_out_button = QtWidgets.QPushButton(self.left_widget)
        self.zoom_out_button.setObjectName("zoomOutButton")
        self.zoom_out_button.setText("-")
        self.zoom_out_button.clicked.connect(self.zoom_out_button_clicked)
        self.grid_layout.addWidget(self.zoom_out_button, 0, 0, 1, 1)

        self.up_button = QtWidgets.QPushButton(self.left_widget)
        self.up_button.setObjectName("upButton")
        self.up_button.setText("up")
        self.up_button.clicked.connect(self.up_button_clicked)
        self.grid_layout.addWidget(self.up_button, 0, 1, 1, 1)

        self.zoom_in_button = QtWidgets.QPushButton(self.left_widget)
        self.zoom_in_button.setObjectName("zoomInButton")
        self.zoom_in_button.setText("+")
        self.zoom_in_button.clicked.connect(self.zoom_in_button_clicked)
        self.grid_layout.addWidget(self.zoom_in_button, 0, 2, 1, 1)

        self.left_button = QtWidgets.QPushButton(self.left_widget)
        self.left_button.setObjectName("leftButton")
        self.left_button.setText("left")
        self.left_button.clicked.connect(self.left_button_clicked)
        self.grid_layout.addWidget(self.left_button, 1, 0, 1, 1)

        self.right_button = QtWidgets.QPushButton(self.left_widget)
        self.right_button.setObjectName("rightButton")
        self.right_button.setText("right")
        self.right_button.clicked.connect(self.right_button_clied)
        self.grid_layout.addWidget(self.right_button, 1, 2, 1, 1)

        self.rotate_left_button = QtWidgets.QPushButton(self.left_widget)
        self.rotate_left_button.setObjectName("rotateLeftButton")
        self.rotate_left_button.setText("rot. left")
        self.rotate_left_button.clicked.connect(self.rotate_left_button_clicked)
        self.grid_layout.addWidget(self.rotate_left_button, 2, 0, 1, 1)

        self.down_button = QtWidgets.QPushButton(self.left_widget)
        self.down_button.setObjectName("downButton")
        self.down_button.setText("down")
        self.down_button.clicked.connect(self.down_button_clicked)
        self.grid_layout.addWidget(self.down_button, 2, 1, 1, 1)

        self.rotate_right_button = QtWidgets.QPushButton(self.left_widget)
        self.rotate_right_button.setObjectName("rotateRightButton")
        self.rotate_right_button.setText("rot. right")
        self.rotate_right_button.clicked.connect(self.rotate_right_button_clicked)
        self.grid_layout.addWidget(self.rotate_right_button, 2, 2, 1, 1)

        self.vertical_layout.addLayout(self.grid_layout)

        # Widget for the layout in the right side of the UI
        self.right_widget = QtWidgets.QWidget(self.centralWidget)
        self.right_widget.setGeometry(QtCore.QRect(321, 15, 661, 571))
        self.right_widget.setObjectName("rightWidget")

        # Vertical layout in the right side of the UI
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.right_widget)
        self.vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_2.setObjectName("verticalLayout_2")

        # Viewport label
        self.viewport_label = QtWidgets.QLabel(self.right_widget)
        self.viewport_label.setFont(font)
        self.viewport_label.setObjectName("viewportLabel")
        self.viewport_label.setText("Viewport")
        self.vertical_layout_2.addWidget(self.viewport_label)

        # Viewport widget
        self.viewport_widget = QtWidgets.QGraphicsView(self.right_widget)
        self.viewport_widget.setFixedWidth(660)
        self.viewport_widget.setFixedHeight(340)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.viewport_widget.setSizePolicy(size_policy)
        self.viewport_widget.setObjectName("viewportWidget")
        self.vertical_layout_2.addWidget(self.viewport_widget)

        # Text console for debugging
        self.text_console = QtWidgets.QTextBrowser(self.right_widget)
        self.text_console.setObjectName("textConsole")
        self.vertical_layout_2.addWidget(self.text_console)

        # Top-level horizontal layout
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontal_layout_2.setObjectName("horizontalLayout_2")
        self.horizontal_layout_2.addWidget(self.left_widget)
        self.horizontal_layout_2.addWidget(self.right_widget)

        self.setCentralWidget(self.centralWidget)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.row_data = []

    def add_button_clicked(self):
        dialog = InputDialog(self)
        dialog.data_submitted.connect(self.add_row)
        dialog.exec()
    
    def add_row(self, graphical_object):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(graphical_object.type))
        self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(graphical_object.name))
        self.row_data.append(graphical_object)  # Store the data
        print(self.row_data[-1].__dict__)

    def remove_button_clicked(self):
        current_row = self.table_widget.currentRow()
        if current_row >= 0:
            self.table_widget.removeRow(current_row)
            del self.row_data[current_row]

    def clear_button_clicked(self):
        self.table_widget.clearContents()
        self.table_widget.setRowCount(0)
        self.row_data.clear()

    def up_button_clicked(self):
        ...

    def down_button_clicked(self):
        ...

    def left_button_clicked(self):
        ...

    def right_button_clied(self):
        ...

    def zoom_out_button_clicked(self):
        ...

    def zoom_in_button_clicked(self):
        ...

    def rotate_left_button_clicked(self):
        ...

    def rotate_right_button_clicked(self):
        ...
