import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(1000, 600)
        self.setObjectName("mainWindow")
        self.setWindowTitle("Sistema Gráfico Interativo")

        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        # Font for the labels
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)

        # Widget for the layout in the left side of the UI
        self.leftWidget = QtWidgets.QWidget(self.centralWidget)
        self.leftWidget.setGeometry(QtCore.QRect(11, 10, 256, 431))
        self.leftWidget.setObjectName("widgetLeft")

        # Vertical layout in the left side of the UI
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Objects table label
        self.objTableLabel = QtWidgets.QLabel(self.leftWidget)
        self.objTableLabel.setFont(font)
        self.objTableLabel.setScaledContents(False)
        self.objTableLabel.setObjectName("objTableLabel")
        self.objTableLabel.setText("Objects")

        self.verticalLayout.addWidget(self.objTableLabel)

        # Objects table (type, name)
        self.tableWidget = QtWidgets.QTableWidget(self.leftWidget)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
    
        item = QtWidgets.QTableWidgetItem()
        item.setText("Type")
        self.tableWidget.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Name")
        self.tableWidget.setHorizontalHeaderItem(1, item)

        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout.addWidget(self.tableWidget)

        # Add, remove and clear buttons in a horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.addButton = QtWidgets.QPushButton(self.leftWidget)
        self.addButton.setObjectName("addButton")
        self.addButton.setText("Add")
        self.horizontalLayout.addWidget(self.addButton)

        self.removeButton = QtWidgets.QPushButton(self.leftWidget)
        self.removeButton.setObjectName("removeButton")
        self.removeButton.setText("Remove")
        self.horizontalLayout.addWidget(self.removeButton)

        self.clearButton = QtWidgets.QPushButton(self.leftWidget)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.setText("Clear")
        self.horizontalLayout.addWidget(self.clearButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Espaço entre os layouts
        self.verticalLayout.addItem(QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed))

        # Control label
        self.controlLabel = QtWidgets.QLabel(self.leftWidget)
        self.controlLabel.setFont(font)
        self.controlLabel.setObjectName("controlLabel")
        self.controlLabel.setText("Control")

        self.verticalLayout.addWidget(self.controlLabel)

        # Control buttons in a grid layout:
        #   Zoom in,   up, zoom out
        #      left,     , right
        # rot. left, down, rot. right

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.zoomOutButton = QtWidgets.QPushButton(self.leftWidget)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.zoomOutButton.setText("-")
        self.gridLayout.addWidget(self.zoomOutButton, 0, 0, 1, 1)

        self.upButton = QtWidgets.QPushButton(self.leftWidget)
        self.upButton.setObjectName("upButton")
        self.upButton.setText("up")
        self.gridLayout.addWidget(self.upButton, 0, 1, 1, 1)

        self.zoomInButton = QtWidgets.QPushButton(self.leftWidget)
        self.zoomInButton.setObjectName("zoomInButton")
        self.zoomInButton.setText("+")
        self.gridLayout.addWidget(self.zoomInButton, 0, 2, 1, 1)

        self.leftButton = QtWidgets.QPushButton(self.leftWidget)
        self.leftButton.setObjectName("leftButton")
        self.leftButton.setText("left")
        self.gridLayout.addWidget(self.leftButton, 1, 0, 1, 1)

        self.rightButton = QtWidgets.QPushButton(self.leftWidget)
        self.rightButton.setObjectName("rightButton")
        self.rightButton.setText("right")
        self.gridLayout.addWidget(self.rightButton, 1, 2, 1, 1)

        self.rotateLeftButton = QtWidgets.QPushButton(self.leftWidget)
        self.rotateLeftButton.setObjectName("rotateLeftButton")
        self.rotateLeftButton.setText("rot. left")
        self.gridLayout.addWidget(self.rotateLeftButton, 2, 0, 1, 1)

        self.downButton = QtWidgets.QPushButton(self.leftWidget)
        self.downButton.setObjectName("downButton")
        self.downButton.setText("down")
        self.gridLayout.addWidget(self.downButton, 2, 1, 1, 1)

        self.rotateRightButton = QtWidgets.QPushButton(self.leftWidget)
        self.rotateRightButton.setObjectName("rotateRightButton")
        self.rotateRightButton.setText("rot. right")
        self.gridLayout.addWidget(self.rotateRightButton, 2, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        # Widget for the layout in the right side of the UI
        self.rightWidget = QtWidgets.QWidget(self.centralWidget)
        self.rightWidget.setGeometry(QtCore.QRect(321, 15, 661, 571))
        self.rightWidget.setObjectName("rightWidget")

        # Vertical layout in the right side of the UI
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.rightWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Viewport label
        self.viewportLabel = QtWidgets.QLabel(self.rightWidget)
        self.viewportLabel.setFont(font)
        self.viewportLabel.setObjectName("viewportLabel")
        self.viewportLabel.setText("Viewport")
        self.verticalLayout_2.addWidget(self.viewportLabel)

        # Viewport widget
        self.viewportWidget = QtWidgets.QGraphicsView(self.rightWidget)
        self.viewportWidget.setFixedWidth(660)
        self.viewportWidget.setFixedHeight(340)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.viewportWidget.setSizePolicy(sizePolicy)
        self.viewportWidget.setObjectName("viewportWidget")
        self.verticalLayout_2.addWidget(self.viewportWidget)

        # Text console for debugging
        self.textConsole = QtWidgets.QTextBrowser(self.rightWidget)
        self.textConsole.setObjectName("textConsole")
        self.verticalLayout_2.addWidget(self.textConsole)

        # Top-level horizontal layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.addWidget(self.leftWidget)
        self.horizontalLayout_2.addWidget(self.rightWidget)

        self.setCentralWidget(self.centralWidget)

        QtCore.QMetaObject.connectSlotsByName(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
