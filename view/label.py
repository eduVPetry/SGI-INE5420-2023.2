from PyQt5.QtWidgets import QLabel


class Label(QLabel):

    def __init__(self, text, font, parent=None):
        super().__init__(parent)
        self.text = text
        self.font = font
        self.init_ui()

    def init_ui(self):
        self.setText(self.text)
        self.setFont(self.font)
