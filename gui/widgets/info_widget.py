from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class InfoWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.label = QLabel("Waiting for game...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def set_message(self, message: str):
        self.label.setText(message)

    def clear(self):
        self.label.setText("")
