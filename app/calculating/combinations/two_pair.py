from calculating.base_odds import BaseOddsCalculator


class TwoPairOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        rank_counts = self.count_ranks()

        counts = sorted(
            rank_counts.values(),
            reverse=True
        )

        if counts[0] >= 2 and len(counts) >= 2:

            paired_ranks = sum(
                1
                for count in counts
                if count >= 2
            )

            if paired_ranks >= 2:
                return 100.0

            if counts[0] >= 3:
                return 100.0

        if counts[0] == 2:

            pair_rank = None

            for rank, count in (
                rank_counts.items()
            ):

                if count == 2:
                    pair_rank = rank
                    break

            outs = 0

            for rank, count in (
                rank_counts.items()
            ):

                if rank == pair_rank:
                    continue

                outs += 4 - count

            return self.calculate_probability(
                outs=outs,
                unseen_cards=self.unseen_cards_count,
                cards_to_come=self.cards_to_come
            )

        return 0.0