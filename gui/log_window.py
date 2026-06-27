from datetime import datetime
from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class LogWindow(QWidget):

    MAX_LINES = 400

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logs")

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        self.text.document().setMaximumBlockCount(self.MAX_LINES)

        layout = QVBoxLayout()

        layout.addWidget(self.text)

        self.setLayout(layout)

    def clean_log(self):
        self.text.clear()

    def add_log(self, message: str):
        self.text.append(message)

        document = self.text.document()

        while document.blockCount() > self.MAX_LINES:

            timestamp = datetime.now().strftime("%H:%M:%S")

            self.text.append(f"[{timestamp}] {message}")

            scrollbar = self.text.verticalScrollBar()

            scrollbar.setValue(scrollbar.maximum())
