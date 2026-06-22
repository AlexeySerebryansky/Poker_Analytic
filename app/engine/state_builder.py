from engine.state import GameState
from engine.cards_grouper import GroupedCards


class StateBuilder:

    def __init__(self):
        self._state = GameState()

    def update(self, grouped_cards: GroupedCards) -> GameState:

        if not self._is_valid(grouped_cards):
            return self._state

        hand = [card.card for card in grouped_cards.hand]
        board = [card.card for card in grouped_cards.board]

        self._state.set_hand(hand)
        self._state.set_board(board)

        return self._state

    def _is_valid(self, grouped_cards: GroupedCards) -> bool:

        hand_count = len(grouped_cards.hand)
        board_count = len(grouped_cards.board)

        return hand_count == 2 and board_count in (0, 3, 4, 5)
