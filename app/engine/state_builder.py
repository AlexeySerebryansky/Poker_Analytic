from engine.state import GameState
from engine.cards_grouper import GroupedCards
from exeptions.exeptions.duplicated_card_error import DuplicatedCardError
from exeptions.exeptions.hand_count_error import HandCountError
from exeptions.exeptions.board_count_error import BoardCountError


class StateBuilder:

    def build(self, grouped_cards: GroupedCards) -> GameState:

        hand = tuple(card.card for card in grouped_cards.hand)
        board = tuple(card.card for card in grouped_cards.board)

        self._validate_hand(hand)
        self._validate_board(board)
        self._validate_duplicates(hand, board)

        return GameState(
            hand=hand,
            board=board
        )

    def _validate_hand(self, hand:list):
        if len(hand) != 2:
            raise HandCountError(len(hand))

    def _validate_board(self, board:list):

        if len(board) not in (0, 3, 4, 5):
            raise BoardCountError(len(board))

    def _validate_duplicates(self, hand:list, board:list):

        cards = hand + board

        duplicates = {
            card
            for card in cards
            if cards.count(card) > 1
        }

        if duplicates:
            raise DuplicatedCardError(sorted(duplicates))