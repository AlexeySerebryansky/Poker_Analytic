from dataclasses import dataclass

from calculating.combinations import (
    PairOddsCalculator,
    TwoPairOddsCalculator,
    SetOddsCalculator,
    StraightOddsCalculator,
    FlushOddsCalculator,
    FullHouseOddsCalculator,
    KareOddsCalculator,
    StreetFlashOddsCalculator,
    FlushRoyalOddsCalculator,
)


@dataclass
class OddsResult:
    pair: float
    two_pair: float
    set: float
    straight: float
    flush: float
    full_house: float
    kare: float
    straight_flush: float
    royal_flush: float


class OddsCalculatorService:

    def calculate(self, game) -> dict[str, float]:

        return {
            "Pair": PairOddsCalculator(game).calculate(),
            "Two Pair": TwoPairOddsCalculator(game).calculate(),
            "Set": SetOddsCalculator(game).calculate(),
            "Straight": StraightOddsCalculator(game).calculate(),
            "Flush": FlushOddsCalculator(game).calculate(),
            "Full House": FullHouseOddsCalculator(game).calculate(),
            "Kare": KareOddsCalculator(game).calculate(),
            "Straight Flush": StreetFlashOddsCalculator(game).calculate(),
            "Royal Flush": FlushRoyalOddsCalculator(game).calculate(),
        }
