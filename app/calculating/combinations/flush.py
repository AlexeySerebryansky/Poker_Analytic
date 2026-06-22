from calculating.base_odds import BaseOddsCalculator


class FlushOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        suit_counts = self.count_suits()

        max_suit_count = max(
            suit_counts.values()
        )

        unseen = self.unseen_cards_count

        if max_suit_count >= 5:
            return 100.0

        if max_suit_count == 4:
            outs = 13 - max_suit_count

            return self.calculate_probability(
                outs=outs,
                unseen_cards=unseen,
                cards_to_come=self.cards_to_come
            )

        if max_suit_count == 3 and self.cards_to_come == 2:
            remaining_suit_cards = (13 - max_suit_count)

            return self.calculate_probability(
                outs=remaining_suit_cards,
                unseen_cards=unseen,
                cards_to_come=2
            )

        return 0.0
