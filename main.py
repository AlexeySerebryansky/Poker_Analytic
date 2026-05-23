from app.engine.combinations import (FlushOddsCalculator,
                                     PairOddsCalculator,
                                     TwoPairOddsCalculator,
                                     SetOddsCalculator)
from app.engine.state import GameState

game = GameState()

game.set_hand(["Ah", "Qd"])

game.set_board([
    "Qh",
    "2c",
    "9h"
])

flush_calculator = FlushOddsCalculator(game)
pair_calculator = PairOddsCalculator(game)
two_pair_calculator = TwoPairOddsCalculator(game)
set_calculator = SetOddsCalculator(game)

print(f"flush - {flush_calculator.calculate()}")
print(f"pair - {pair_calculator.calculate()}")
print(f"two_pair - {two_pair_calculator.calculate()}")
print(f"set - {set_calculator.calculate()}")
