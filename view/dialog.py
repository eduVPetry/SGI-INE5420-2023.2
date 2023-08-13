import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("Dialog")
        self.setWindowTitle("Add Object")
        self.resize(640, 480)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)

        # Tabs
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setGeometry(QtCore.QRect(30, 80, 571, 331))
        self.tab_widget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab_2 = QtWidgets.QWidget()
        self.tab_3 = QtWidgets.QWidget()

        self.tab.setObjectName("tab")
        self.tab_2.setObjectName("tab_2")
        self.tab_3.setObjectName("tab_3")

        self.tab_widget.addTab(self.tab, "")
        self.tab_widget.addTab(self.tab_2, "")
        self.tab_widget.addTab(self.tab_3, "")

        self.tab_widget.setTabText(0, "Point")
        self.tab_widget.setTabText(1, "Line")
        self.tab_widget.setTabText(2, "Wireframe")

        self.tab_widget.setCurrentIndex(0)

        # Ok and Cancel Buttons
        self.button_box = QtWidgets.QDialogButtonBox(self)
        self.button_box.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("buttonBox")
        self.button_box.accepted.connect(self.ok_callback)
        self.button_box.rejected.connect(self.cancel_callback)

        # Fonts for the labels
        font = QtGui.QFont()
        font.setPointSize(10)

        font_bold = QtGui.QFont()
        font_bold.setPointSize(10)
        font_bold.setBold(True)

        # Labels
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 10, 57, 15))
        self.label.setFont(font_bold)
        self.label.setText("Name")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 16, 16))
        self.label_2.setFont(font)
        self.label_2.setText("x")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(230, 90, 57, 15))
        self.label_3.setFont(font)
        self.label_3.setText("y")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 91, 31))
        self.label_4.setFont(font_bold)
        self.label_4.setText("Start Point")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.label_5.setFont(font_bold)
        self.label_5.setText("End Point")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(220, 80, 57, 15))
        self.label_6.setFont(font)
        self.label_6.setText("y1")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(50, 80, 16, 16))
        self.label_7.setFont(font)
        self.label_7.setText("x1")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(220, 200, 57, 15))
        self.label_8.setFont(font)
        self.label_8.setText("y2")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(50, 200, 16, 16))
        self.label_9.setFont(font)
        self.label_9.setText("x2")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(40, 30, 141, 16))
        self.label_10.setFont(font_bold)
        self.label_10.setText("Point Coordinates")
        self.label_10.setObjectName("label_10")

        # Plain text inputs
        self.plain_text_input = QtWidgets.QLineEdit(self)
        self.plain_text_input.setGeometry(QtCore.QRect(30, 30, 191, 31))
        self.plain_text_input.setObjectName("plainTextEdit")

        self.plain_text_input_2 = QtWidgets.QLineEdit(self.tab)
        self.plain_text_input_2.setGeometry(QtCore.QRect(80, 80, 111, 31))
        self.plain_text_input_2.setObjectName("plainTextEdit_2")

        self.plain_text_input_3 = QtWidgets.QLineEdit(self.tab)
        self.plain_text_input_3.setGeometry(QtCore.QRect(250, 80, 111, 31))
        self.plain_text_input_3.setObjectName("plainTextEdit_3")

        self.plain_text_input_4 = QtWidgets.QLineEdit(self.tab_2)
        self.plain_text_input_4.setGeometry(QtCore.QRect(240, 70, 111, 31))
        self.plain_text_input_4.setObjectName("plainTextEdit_4")

        self.plain_text_input_5 = QtWidgets.QLineEdit(self.tab_2)
        self.plain_text_input_5.setGeometry(QtCore.QRect(70, 70, 111, 31))
        self.plain_text_input_5.setObjectName("plainTextEdit_5")

        self.plain_text_input_6 = QtWidgets.QLineEdit(self.tab_2)
        self.plain_text_input_6.setGeometry(QtCore.QRect(240, 190, 111, 31))
        self.plain_text_input_6.setObjectName("plainTextEdit_6")

        self.plain_text_input_7 = QtWidgets.QLineEdit(self.tab_2)
        self.plain_text_input_7.setGeometry(QtCore.QRect(70, 190, 111, 31))
        self.plain_text_input_7.setObjectName("plainTextEdit_7")

        QtCore.QMetaObject.connectSlotsByName(self)

    def ok_callback(self):
        print("OK")
        self.close()
    
    def cancel_callback(self):
        print("CANCEL")
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())
