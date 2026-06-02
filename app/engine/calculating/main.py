from engine.calculating.combinations import (
    FlushOddsCalculator,
    PairOddsCalculator,
    TwoPairOddsCalculator,
    SetOddsCalculator,
    FullHouseOddsCalculator,
    KareOddsCalculator,
    StraightOddsCalculator,
    StreetFlashOddsCalculator,
    FlushRoyalOddsCalculator
)
from engine.calculating.state import GameState

game = GameState()


game.set_hand(["Qd", "Jc"])

game.set_board([
    "Qh",
    "2h",
    "9h"
])

print("=" * 60)
print(f"Hand: {' '.join(game.hand)}")
print(f"Board: {' '.join(game.board)}")
print("=" * 60)

print(f"Pair:           {PairOddsCalculator(game).calculate()}%")
print(f"Two Pair:       {TwoPairOddsCalculator(game).calculate()}%")
print(f"Set:            {SetOddsCalculator(game).calculate()}%")
print(f"Straight:       {StraightOddsCalculator(game).calculate()}%")
print(f"Flush:          {FlushOddsCalculator(game).calculate()}%")
print(f"Full House:     {FullHouseOddsCalculator(game).calculate()}%")
print(f"Kare:           {KareOddsCalculator(game).calculate()}%")
print(f"Straight Flush: {StreetFlashOddsCalculator(game).calculate()}%")
print(f"Royal Flush:    {FlushRoyalOddsCalculator(game).calculate()}%")
