from dataclasses import dataclass

from detection.detect_cards import DetectedCard
from engine.detection_matcher import RecognizedCard


@dataclass(frozen=True)
class GroupedCards:

    hand: list[RecognizedCard]

    board: list[RecognizedCard]


class CardGrouper:

    def group(self, cards: list[RecognizedCard]) -> GroupedCards:

        count = len(cards)

        if count < 2:
            return GroupedCards(hand=[], board=[])

        if count == 2:
            return GroupedCards(hand=cards, board=[])

        if count <= 7 :

            sorted_cards = sorted(
                cards,
                key=lambda card: card.detection.center_y
            )

            return GroupedCards(hand=sorted_cards[-2:], board=sorted_cards[:-2])

        else:
            raise ValueError(f"Unexpected number of cards: {len(cards)}")




