from PyQt5.QtWidgets import QPushButton

from view.input_dialog import InputDialog


class AddButton(QPushButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setText("Add")
        self.clicked.connect(self.clicked_callback)

    def clicked_callback(self):
        main_window = self.parent().parent().parent()
        dialog = InputDialog(main_window)
        dialog.data_submitted.connect(main_window.display_file.add)
        dialog.exec()
