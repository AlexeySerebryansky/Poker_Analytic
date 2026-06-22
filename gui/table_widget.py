from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout
)

from gui.card_widget import CardsWidget
from gui.odds_widget import OddsWidget


class TableWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.cards_widget = CardsWidget()
        self.odds_widget = OddsWidget()

        layout = QVBoxLayout()

        layout.addWidget(
            self.cards_widget
        )

        layout.addWidget(
            self.odds_widget
        )

        self.setLayout(layout)

    def update_state(self, game, odds):
        self.cards_widget.update_cards(
            game.hand,
            game.board
        )

        self.odds_widget.update_odds(
            odds
        )
