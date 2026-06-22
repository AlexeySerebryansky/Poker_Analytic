from calculating.combinations import (
    FlushOddsCalculator,
    PairOddsCalculator,
    TwoPairOddsCalculator,
    SetOddsCalculator,
    FullHouseOddsCalculator,
    KareOddsCalculator,
    StraightOddsCalculator,
    StreetFlashOddsCalculator,
    FlushRoyalOddsCalculator,
)

from engine.state import GameState

print("=" * 70)
print("TEST 1: Full House - set + need pair")
print("=" * 70)
game1 = GameState()
game1.set_hand(["Ah", "Ad"])
game1.set_board(["Ac", "Kh", "2c"])

fh_calc = FullHouseOddsCalculator(game1)
print(f"Hand: {game1.hand}, Board: {game1.board}")
print(f"Result: {fh_calc.calculate()}%")
print("Have set of aces, need any pair")
print()

print("=" * 70)
print("TEST 2: Full House - two pairs + need set")
print("=" * 70)
game2 = GameState()
game2.set_hand(["Ah", "Kd"])
game2.set_board(["Ac", "Kh", "2c"])

fh_calc2 = FullHouseOddsCalculator(game2)
print(f"Hand: {game2.hand}, Board: {game2.board}")
print(f"Result: {fh_calc2.calculate()}%")
print("Have two pairs (aces and kings), need one more ace or king")
print()

print("=" * 70)
print("TEST 3: Kare - from set")
print("=" * 70)
game3 = GameState()
game3.set_hand(["Ah", "Ad"])
game3.set_board(["Ac", "Kh", "2c"])

kare_calc = KareOddsCalculator(game3)
print(f"Hand: {game3.hand} Board: {game3.board}")
print(f"Result: {kare_calc.calculate()}%")
print("Have set of aces, need 1 more ace (1 out)")
print()

print("=" * 70)
print("TEST 4: Kare - from pair on flop")
print("=" * 70)
game4 = GameState()
game4.set_hand(["Ah", "Ad"])
game4.set_board(["Kh", "Qc", "2c"])

kare_calc2 = KareOddsCalculator(game4)
print(f"Hand: {game4.hand}, Board: {game4.board}")
print(f"Result: {kare_calc2.calculate()}%")
print("Have pair of aces, need both remaining aces")
print()

print("=" * 70)
print("TEST 5: Straight - open-ended straight draw")
print("=" * 70)
game5 = GameState()
game5.set_hand(["9h", "8d"])
game5.set_board(["7c", "6h", "2c"])

straight_calc = StraightOddsCalculator(game5)
print(f"Hand: {game5.hand}, Board: {game5.board}")
print(f"Result: {straight_calc.calculate()}%")
print("Have 6-7-8-9, need 5 or T (8 outs)")
print()

print("=" * 70)
print("TEST 6: Straight - gutshot")
print("=" * 70)
game6 = GameState()
game6.set_hand(["9h", "7d"])
game6.set_board(["6c", "5h", "2c"])

straight_calc2 = StraightOddsCalculator(game6)
print(f"Hand: {game6.hand}, Board: {game6.board}")
print(f"Result: {straight_calc2.calculate()}%")
print("Have 5-6-7-9, need 8 (4 outs)")
print()

print("=" * 70)
print("TEST 7: Straight Flush - draw")
print("=" * 70)
game7 = GameState()
game7.set_hand(["9h", "8h"])
game7.set_board(["7h", "6h", "2c"])

sf_calc = StreetFlashOddsCalculator(game7)
print(f"Hand: {game7.hand}, Board: {game7.board}")
print(f"Result: {sf_calc.calculate()}%")
print("Have 6h-7h-8h-9h, need 5h or Th (2 outs)")
print()

print("=" * 70)
print("TEST 8: Royal Flush - draw")
print("=" * 70)
game8 = GameState()
game8.set_hand(["Ah", "Kh"])
game8.set_board(["Qh", "Jh", "2c"])

rf_calc = FlushRoyalOddsCalculator(game8)
print(f"Hand: {game8.hand}, Board: {game8.board}")
print(f"Result: {rf_calc.calculate()}%")
print("Have Ah-Kh-Qh-Jh, need Th (1 out)")
print()

print("=" * 70)
print("SUMMARY: All combinations from main.py")
print("=" * 70)
game = GameState()
game.set_hand(["Ah", "Qd"])
game.set_board(["Qh", "2c", "9h"])

print(f"Hand: {game.hand}, Board: {game.board}")
print(f"flush: {FlushOddsCalculator(game).calculate()}%")
print(f"pair: {PairOddsCalculator(game).calculate()}%")
print(f"two_pair: {TwoPairOddsCalculator(game).calculate()}%")
print(f"set: {SetOddsCalculator(game).calculate()}%")
print(f"full_house: {FullHouseOddsCalculator(game).calculate()}%")
print(f"kare: {KareOddsCalculator(game).calculate()}%")
print(f"straight: {StraightOddsCalculator(game).calculate()}%")
print(f"straight_flush: {StreetFlashOddsCalculator(game).calculate()}%")
print(f"royal_flush: {FlushRoyalOddsCalculator(game).calculate()}%")
