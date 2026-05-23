from abc import ABC, abstractmethod
from collections import Counter


class BaseOddsCalculator(ABC):

    def __init__(self, game_state):

        self.game_state = game_state

    @property
    def hand(self):

        return self.game_state.hand

    @property
    def board(self):

        return self.game_state.board

    @property
    def cards(self):

        return self.game_state.all_cards

    @property
    def unseen_cards_count(self):

        return 52 - len(self.cards)

    @property
    def cards_to_come(self):

        if self.game_state.street == "flop":
            return 2

        if self.game_state.street == "turn":
            return 1

        return 0

    def count_ranks(self):

        ranks = [
            card[0]
            for card in self.cards
        ]

        return Counter(ranks)

    def count_suits(self):

        suits = [
            card[1]
            for card in self.cards
        ]

        return Counter(suits)

    @staticmethod
    def calculate_probability(
        outs,
        unseen_cards,
        cards_to_come
    ):

        if cards_to_come == 2:

            probability = (
                1 -
                (
                    (unseen_cards - outs)
                    / unseen_cards
                )
                *
                (
                    (unseen_cards - outs - 1)
                    / (unseen_cards - 1)
                )
            )

        elif cards_to_come == 1:

            probability = (
                outs / unseen_cards
            )

        else:

            probability = 0.0

        return round(
            probability * 100,
            2
        )

    @abstractmethod
    def calculate(self):

        pass