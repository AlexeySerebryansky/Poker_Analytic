from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QMainWindow, QWidget

from gui.card_widget import CardsWidget
from gui.log_window import LogWindow
from gui.odds_widget import OddsWidget
from gui.pipeline_worker import PipelineWorker


class TableWidget(QMainWindow):

    def __init__(self, selected_window, capture):
        super().__init__()

        self.setWindowTitle(selected_window.title)
        self.setMinimumSize(400, 300)

        self.cards_widget = CardsWidget()
        self.odds_widget = OddsWidget()

        self.log_window = LogWindow()

        self.worker = PipelineWorker(selected_window, capture)

        self.worker.state_updated.connect(self.update_state)
        self.worker.log_updated.connect(self.log_window.add_log)


        self.logs_btn = QPushButton("Logs")
        self.logs_btn.clicked.connect(self.log_window.show)

        central  =QWidget()

        layout = QVBoxLayout()

        layout.addWidget(self.cards_widget)
        layout.addWidget(self.odds_widget)
        layout.addWidget(self.logs_btn)

        central.setLayout(layout)

        self.setCentralWidget(central)

        self.worker.start()


    def update_state(self, game, odds):
        self.cards_widget.update_cards(game.hand, game.board)

        self.odds_widget.update_odds(odds)
