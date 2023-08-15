from PyQt5.QtWidgets import QPlainTextEdit

class DebugConsole(QPlainTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setReadOnly(True)
    
    def show_debug_message(self, debug_message):
        self.appendPlainText(debug_message)
