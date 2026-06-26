import keyboard
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QApplication,
)

from gui.log_window import LogWindow
from gui.pipeline_worker import PipelineWorker
from gui.stream_desctop import CaptureThread
from gui.table_widget import TableWidget
from stream_from_descktop.capture import ScreenCapture, CaptureConfig

from stream_from_descktop.windows_utils import WindowSelector


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Poker Assistant")

        self.resize(500, 400)

        self.table = []

        self.layout = QVBoxLayout()

        buttons_layout = QHBoxLayout()

        self.add_button(self.layout, "Add Table", self.add_table)
        self.add_button(buttons_layout, "log", self.show_logs)
        self.add_button(buttons_layout, "Settings", self.settings)

        self.layout.addLayout(buttons_layout)

        self.status_label = QLabel("Press Add Table")
        self.layout.addWidget(self.status_label)

        central = QWidget()

        central.setLayout(self.layout)

        self.setCentralWidget(central)

        self.log_window = LogWindow()

        self.capture = ScreenCapture(
            CaptureConfig(fps=15, region=None)
        )

        self.capture_thread = CaptureThread(self.capture)
        self.capture_thread.start()

    def add_table(self):
        self.log("add table")

        self.set_status("Move cursor over poker table and press F8")

        QApplication.processEvents()

        keyboard.wait("F8")

        selected_window = WindowSelector.select_window()

        self.log(f"Selected window: {selected_window.title}")

        self.set_status(f"Selected window: {selected_window.title}")

        table = TableWidget()

        worker = PipelineWorker(selected_window, self.capture_thread)

        self.log("worker created")

        worker.state_updated.connect(table.update_state)

        worker.log_updated.connect(self.log_window.add_log)

        worker.start()

        self.log("worker started")

        self.set_status(f"Tracking: {selected_window.title}")

        self.table.append({"widget": table, "worker": worker})
        self.layout.addWidget(table)

    def set_status(self, text: str):
        self.status_label.setText(text)

    def add_button(self, layout, text, callback):
        button = QPushButton(text)

        button.clicked.connect(callback)

        layout.addWidget(button)

        return button

    def log(self, massage: str):
        self.log_window.add_log(massage)

    def show_logs(self):
        self.log_window.show()

    def settings(self):
        print("Settings")
