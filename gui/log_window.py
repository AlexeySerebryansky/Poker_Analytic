from datetime import datetime
from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout


class LogWindow(QWidget):

    MAX_LINES = 1000

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logs")

        self.text = QTextEdit()

        self.text.setReadOnly(True)

        layout = QVBoxLayout()

        layout.addWidget(self.text)

        self.setLayout(layout)

    def clean_log(self):
        self.text.clear()

    def add_log(self, message: str):
        self.text.append(message)

        document = self.text.document()

        while document.blockCount() > self.MAX_LINES:
            cursor = self.text.textCursor()

            cursor.movePosition(cursor.MoveOperation.Start)
            cursor.select(cursor.SelectionType.BlockUnderCursor)
            cursor.removeSelectedText()
            cursor.deleteChar()

            timestamp = datetime.now().strftime("%H:%M:%S")

            self.text.append(f"[{timestamp}] {message}")

            self.text.verticalScrollBar().setValue(
                self.text.verticalScrollBar().maximum()
            )
