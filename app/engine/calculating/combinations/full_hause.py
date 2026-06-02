from math import comb
from engine.calculating.base_odds import BaseOddsCalculator


class FullHouseOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        rank_counts = self.count_ranks()

        counts = sorted(
            rank_counts.values(),
            reverse=True
        )

        if counts[0] >= 3 and len(counts) >= 2 and counts[1] >= 2:
            return 100.0

        if counts[0] == 3:

            set_rank = None
            for rank, count in rank_counts.items():
                if count == 3:
                    set_rank = rank
                    break

            outs = 0

            for rank, count in rank_counts.items():
                if rank != set_rank:
                    remaining = 4 - count
                    outs += remaining

            return self.calculate_probability(
                outs=outs,
                unseen_cards=self.unseen_cards_count,
                cards_to_come=self.cards_to_come
            )

        if counts[0] == 2 and len(counts) >= 2 and counts[1] == 2:

            pair_ranks = []
            for rank, count in rank_counts.items():
                if count == 2:
                    pair_ranks.append(rank)

            outs = 0

            for rank in pair_ranks:
                remaining = 4 - rank_counts[rank]
                outs += remaining

            return self.calculate_probability(
                outs=outs,
                unseen_cards=self.unseen_cards_count,
                cards_to_come=self.cards_to_come
            )

        if counts[0] == 2:

            if self.cards_to_come == 1:
                return 0.0

            pair_rank = None
            for rank, count in rank_counts.items():
                if count == 2:
                    pair_rank = rank
                    break

            total_runouts = comb(
                self.unseen_cards_count,
                self.cards_to_come
            )

            favorable = 0

            for rank, count in rank_counts.items():
                if rank != pair_rank:
                    remaining = 4 - count

                    if remaining >= 2:
                        favorable += comb(remaining, 2)

            probability = (favorable / total_runouts) * 100

            return round(probability, 2)

        return 0.0
