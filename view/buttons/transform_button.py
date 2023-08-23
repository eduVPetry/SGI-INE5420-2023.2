from PyQt5.QtWidgets import QPushButton

from view.transform_dialog import TransformDialog


class TransformButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Transform")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        dialog = TransformDialog(self.window())
        dialog.exec()
