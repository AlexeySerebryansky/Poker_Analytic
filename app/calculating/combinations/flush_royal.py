from calculating.base_odds import BaseOddsCalculator

class FlushRoyalOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        royal_ranks = {'T', 'J', 'Q', 'K', 'A'}

        if self._has_royal_flush():
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

            royal_cards_present = set(ranks) & royal_ranks

            if len(royal_cards_present) < 3:
                continue

            missing_ranks = royal_ranks - set(ranks)

            if len(missing_ranks) <= self.cards_to_come:

                for rank in missing_ranks:
                    card = rank + suit

                    if card not in self.cards:
                        total_outs.add(card)

        outs = len(total_outs)

        if outs == 0:
            return 0.0

        return self.calculate_probability(
            outs=outs,
            unseen_cards=self.unseen_cards_count,
            cards_to_come=self.cards_to_come
        )

    def _has_royal_flush(self):

        royal_ranks = {'T', 'J', 'Q', 'K', 'A'}

        suits_dict = {}
        for card in self.cards:
            suit = card[1]
            rank = card[0]
            if suit not in suits_dict:
                suits_dict[suit] = []
            suits_dict[suit].append(rank)

        for suit, ranks in suits_dict.items():
            if royal_ranks.issubset(set(ranks)):
                return True

        return False