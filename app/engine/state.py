from app.engine.constants import RANKS, SUITS


class GameState:

    def __init__(self):

        self._hand = []

        self._board = []

    @property
    def hand(self):

        return self._hand

    @property
    def board(self):

        return self._board

    @property
    def all_cards(self):

        return (
                self._hand +
                self._board
        )

    @property
    def street(self):

        streets = {
            3: "flop",
            4: "turn",
            5: "river"
        }

        return streets.get(
            len(self._board)
        )

    def set_hand(self, cards):

        self._validate_cards(cards)
        self._validate_card_format(cards)

        if len(cards) != 2:
            raise ValueError(
                "Hand must contain 2 cards"
            )

        self._hand = cards

    def set_board(self, cards):

        self._validate_cards(cards)
        self._validate_card_format(cards)

        if len(cards) not in (3, 4, 5):
            raise ValueError(
                "Board must contain 3-5 cards"
            )

        self._board = cards

    def reset(self):

        self._hand = []

        self._board = []

    def _validate_cards(self, cards):

        if len(cards) != len(set(cards)):
            raise ValueError(
                "Duplicate cards detected"
            )

    def _validate_card_format(self, cards):

        for card in cards:

            if len(card) != 2:
                raise ValueError(
                    f"Invalid card length: {card}"
                )

            rank = card[0]
            suit = card[1]

            if rank not in RANKS:
                raise ValueError(f"Invalid rank format {rank}")

            if suit not in SUITS:
                raise ValueError(f"Invalid suit format {suit}")

