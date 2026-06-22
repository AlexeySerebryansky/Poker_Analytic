from calculating.base_odds import BaseOddsCalculator


class KareOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        rank_counts = self.count_ranks()

        counts = sorted(
            rank_counts.values(),
            reverse=True
        )

        if counts[0] >= 4:
            return 100.0

        if counts[0] == 3:

            for rank, count in rank_counts.items():
                if count == 3:
                    remaining = 4 - count

                    return self.calculate_probability(
                        outs=remaining,
                        unseen_cards=self.unseen_cards_count,
                        cards_to_come=self.cards_to_come
                    )

        if counts[0] == 2:

            for rank, count in rank_counts.items():
                if count == 2:
                    remaining = 4 - count

                    if self.cards_to_come == 2 and remaining == 2:
                        probability = (
                            (remaining / self.unseen_cards_count)
                            *
                            ((remaining - 1) / (self.unseen_cards_count - 1))
                        )
                        return round(probability * 100, 2)

                    if self.cards_to_come == 1:
                        return 0.0

        return 0.0
