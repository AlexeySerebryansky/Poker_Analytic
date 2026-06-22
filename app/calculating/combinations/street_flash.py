from calculating.base_odds import BaseOddsCalculator
from calculating.constants import RANKS


class StreetFlashOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        if self._has_straight_flush():
            return 100.0

        suits_dict = {}
        for card in self.cards:
            suit = card[1]
            rank = card[0]
            if suit not in suits_dict:
                suits_dict[suit] = []
            suits_dict[suit].append(rank)

        total_outs = set()

        for suit, ranks in suits_dict.items():

            if len(ranks) < 3:
                continue

            rank_indices = sorted([RANKS.index(rank) for rank in ranks])

            all_straights = self._get_all_possible_straights()

            for straight in all_straights:
                missing = straight - set(rank_indices)

                if len(missing) <= self.cards_to_come:

                    for rank_idx in missing:
                        rank = RANKS[rank_idx]
                        card = rank + suit

                        if card not in [c for c in self.cards]:
                            total_outs.add(card)

        outs = len(total_outs)

        if outs == 0:
            return 0.0

        return self.calculate_probability(
            outs=outs,
            unseen_cards=self.unseen_cards_count,
            cards_to_come=self.cards_to_come,
        )

    def _has_straight_flush(self):

        suits_dict = {}
        for card in self.cards:
            suit = card[1]
            rank = card[0]
            if suit not in suits_dict:
                suits_dict[suit] = []
            suits_dict[suit].append(rank)

        for suit, ranks in suits_dict.items():
            if len(ranks) < 5:
                continue

            rank_indices = sorted(set([RANKS.index(rank) for rank in ranks]))

            consecutive = 1
            for i in range(1, len(rank_indices)):
                if rank_indices[i] == rank_indices[i - 1] + 1:
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
