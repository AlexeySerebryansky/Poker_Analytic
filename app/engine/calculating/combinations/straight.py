from itertools import combinations
from engine.calculating.base_odds import BaseOddsCalculator
from engine.calculating.constants import RANKS, SUITS


class StraightOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        if self._has_straight():
            return 100.0

        if self.cards_to_come == 0:
            return 0.0

        all_cards = [rank + suit for rank in RANKS for suit in SUITS]
        unseen_cards = [card for card in all_cards if card not in self.cards]

        favorable = 0
        total = 0

        for future_cards in combinations(unseen_cards, self.cards_to_come):
            total += 1

            test_cards = self.cards + list(future_cards)

            if self._check_straight_in_cards(test_cards):
                favorable += 1

        if total == 0:
            return 0.0

        probability = (favorable / total) * 100

        return round(probability, 2)

    def _check_straight_in_cards(self, cards):

        card_ranks = [card[0] for card in cards]
        rank_indices = sorted(set([RANKS.index(rank) for rank in card_ranks]))

        consecutive = 1
        for i in range(1, len(rank_indices)):
            if rank_indices[i] == rank_indices[i-1] + 1:
                consecutive += 1
                if consecutive >= 5:
                    return True
            else:
                consecutive = 1

        if set([0, 1, 2, 3, 12]).issubset(set(rank_indices)):
            return True

        return False

    def _has_straight(self):

        card_ranks = [card[0] for card in self.cards]
        rank_indices = sorted(set([RANKS.index(rank) for rank in card_ranks]))

        consecutive = 1
        for i in range(1, len(rank_indices)):
            if rank_indices[i] == rank_indices[i-1] + 1:
                consecutive += 1
                if consecutive >= 5:
                    return True
            else:
                consecutive = 1

        if set([0, 1, 2, 3, 12]).issubset(set(rank_indices)):
            return True

        return False

    def _get_all_possible_straights(self):

        straights = []

        for i in range(len(RANKS) - 4):
            straights.append(set(range(i, i + 5)))

        straights.append({0, 1, 2, 3, 12})

        return straights