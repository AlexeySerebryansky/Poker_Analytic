import sys
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from gui.main_window import MainWindow


def main():

    Path("gui/log.txt").write_text("", encoding="utf-8")

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec())



if __name__ == "__main__":
    main()
