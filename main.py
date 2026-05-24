from app.engine.combinations import (
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
from app.engine.state import GameState

game = GameState()

game.set_hand(["Ah", "Kh"])

game.set_board([
    "Qh",
    "2c",
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
