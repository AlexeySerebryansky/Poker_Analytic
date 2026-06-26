from calculating.constants import RANKS, SUITS
from exeptions import duplicated_card_error
from exeptions.duplicated_card_error import DuplicatedCardError


class GameState:

    def __init__(self):

        self._hand = []

        self._board = []

    @property
    def hand(self):

        return tuple(self._hand)

    @property
    def board(self):

        return tuple(self._board)

    @property
    def all_cards(self):

        return self._hand + self._board

    def set_hand(self, cards):

        self._validate_cards(cards)
        self._validate_card_format(cards)

        self._hand = cards

    def set_board(self, cards):

        self._validate_cards(cards)
        self._validate_card_format(cards)

        self._board = cards

    def reset(self):

        self._hand = []
        self._board = []

    @staticmethod
    def _validate_cards(cards):

        if len(cards) != len(set(cards)):
            duplicates = [card for card in set(cards) if cards.count(card) > 1]
            raise DuplicatedCardError(duplicates)

    @staticmethod
    def _validate_card_format(cards):

        for card in cards:

            if len(card) != 2:
                raise ValueError(f"Invalid card length: {card}")

            rank = card[0]
            suit = card[1]

            if rank not in RANKS:
                raise ValueError(f"Invalid rank format {rank}")

            if suit not in SUITS:
                raise ValueError(f"Invalid suit format {suit}")
