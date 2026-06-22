from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class CardsWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.hand_label = QLabel("Hand: -")
        self.board_label = QLabel("Board: -")

        layout = QVBoxLayout()

        layout.addWidget(self.hand_label)
        layout.addWidget(self.board_label)

        self.setLayout(layout)

    def update_cards(self, hand, board):
        self.hand_label.setText(
            f"Hand: {' '.join(hand)}"
        )

        self.board_label.setText(
            f"Board: {' '.join(board)}"
        )
