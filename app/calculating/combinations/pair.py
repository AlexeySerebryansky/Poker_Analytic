from calculating.base_odds import BaseOddsCalculator


class PairOddsCalculator(BaseOddsCalculator):

    def calculate(self):

        rank_counts = self.count_ranks()

        if max(rank_counts.values()) >= 2:
            return 100.0

        outs = 0

        hand_ranks = {card[0] for card in self.hand}

        for rank in hand_ranks:
            remaining = 4 - rank_counts[rank]
            outs += remaining

        board_ranks = {card[0] for card in self.board}

        for rank in board_ranks:
            if rank not in hand_ranks:
                remaining = 4 - rank_counts[rank]
                outs += remaining

        return self.calculate_probability(
            outs=outs,
            unseen_cards=self.unseen_cards_count,
            cards_to_come=self.cards_to_come,
        )
