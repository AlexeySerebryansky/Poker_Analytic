from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)


class OddsWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.table = QTableWidget()

        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels([
            "Combination",
            "Chance"
        ])

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        combinations = [
            "Pair",
            "Two Pair",
            "Set",
            "Straight",
            "Flush",
            "Full House",
            "Kare",
            "Straight Flush",
            "Royal Flush"
        ]

        self.table.setRowCount(len(combinations))

        self.rows = {}

        for row, name in enumerate(combinations):
            self.table.setItem(
                row,
                0,
                QTableWidgetItem(name)
            )

            self.table.setItem(
                row,
                1,
                QTableWidgetItem("0.00%")
            )

            self.rows[name] = row

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)

    def update_odds(self, odds: dict):

        for name, value in odds.items():
            row = self.rows[name]

            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    f"{value:.2f}%"
                )
            )
