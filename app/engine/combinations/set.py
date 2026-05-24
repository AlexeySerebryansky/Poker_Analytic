from math import comb

from app.engine.base_odds import BaseOddsCalculator


class SetOddsCalculator(
    BaseOddsCalculator
):

    def calculate(self):

        rank_counts = self.count_ranks()

        counts = sorted(
            rank_counts.values(),
            reverse=True
        )

        if counts[0] >= 3:
            return 100.0

        total_runouts = comb(
            self.unseen_cards_count,
            self.cards_to_come
        )

        favorable = 0

        if counts[0] == 2:

            pair_rank = None

            for rank, count in (
                rank_counts.items()
            ):

                if count == 2:
                    pair_rank = rank
                    break

            remaining = (
                4 - rank_counts[pair_rank]
            )

            favorable = (
                total_runouts -
                comb(
                    self.unseen_cards_count
                    - remaining,
                    self.cards_to_come
                )
            )

        else:

            if self.cards_to_come == 1:
                return 0.0

            hand_ranks = {
                card[0]
                for card in self.hand
            }

            for rank in hand_ranks:

                remaining = (
                    4 - rank_counts[rank]
                )

                if remaining >= 2:

                    favorable += comb(
                        remaining,
                        2
                    )

        probability = (
            favorable / total_runouts
        ) * 100

        return round(
            probability,
            2
        )