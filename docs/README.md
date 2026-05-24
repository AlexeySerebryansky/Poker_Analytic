# Poker_Analytic

Poker hand probability calculator for Texas Hold'em.

## Description

This project calculates the probability of making each poker hand by the river, independently of each other. The calculator takes into account the player's current hand and the board cards (flop/turn).

## Supported Hands

- **Pair** - two cards of the same rank
- **Two Pair** - two pairs of different ranks
- **Set** (Three of a Kind) - three cards of the same rank
- **Straight** - five consecutive cards by rank
- **Flush** - five cards of the same suit
- **Full House** - three cards of one rank + two cards of another rank
- **Kare** (Four of a Kind) - four cards of the same rank
- **Straight Flush** - five consecutive cards of the same suit
- **Royal Flush** - T-J-Q-K-A of the same suit

## Installation

```bash
# Clone the repository
git clone <repository-url>

# Navigate to project directory
cd Poker_Analytic

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies (if any)
pip install -r requirements.txt
```

## Usage

### Basic Example

```python
from app.engine.combinations import (
    FlushOddsCalculator,
    PairOddsCalculator,
    StraightOddsCalculator
)
from app.engine.state import GameState

# Create game state
game = GameState()

# Set player's hand (2 cards)
game.set_hand(["Ah", "Qd"])

# Set board (3 cards on flop, 4 on turn, 5 on river)
game.set_board(["Qh", "2c", "9h"])

# Calculate probabilities
pair_calc = PairOddsCalculator(game)
print(f"Pair: {pair_calc.calculate()}%")

flush_calc = FlushOddsCalculator(game)
print(f"Flush: {flush_calc.calculate()}%")

straight_calc = StraightOddsCalculator(game)
print(f"Straight: {straight_calc.calculate()}%")
```

### Card Format

Cards are specified in format: `<rank><suit>`

**Ranks:**
- `2-9` - number cards
- `T` - ten
- `J` - jack
- `Q` - queen
- `K` - king
- `A` - ace

**Suits:**
- `h` - hearts
- `d` - diamonds
- `c` - clubs
- `s` - spades

**Examples:** `Ah` (ace of hearts), `Kd` (king of diamonds), `9s` (nine of spades)

## Running the Example

```bash
python main.py
```

Output:
```
============================================================
Hand: Ah Qd
Board: Qh 2c 9h
============================================================
Pair:           100.0%
Two Pair:       34.97%
Set:            8.42%
Straight:       0.0%
Flush:          38.39%
Full House:     0.83%
Kare:           0.09%
Straight Flush: 0.0%
Royal Flush:    0.0%
```

## How It Works

### Independent Probability Calculation

Each calculator computes probability **independently** of other hands. This means:

- **Pair** shows the probability of making at least a pair by the river
- **Flush** shows the probability of making a flush by the river
- And so on for each hand

Probabilities **do not sum to 100%**, as one hand can contain multiple combinations simultaneously (e.g., flush and pair).

### Current State Consideration

Calculators take into account:
- Cards in player's hand
- Cards on the board (flop/turn/river)
- Number of remaining cards in the deck
- Number of cards yet to be dealt

If a hand is already made, the calculator returns 100%.

### Calculation Methods

The project uses two approaches:

1. **Outs Formula** - for simple hands (pair, flush draw)
   ```
   P = 1 - ((unseen - outs) / unseen) * ((unseen - outs - 1) / (unseen - 1))
   ```

2. **Combinatorial Approach** - for complex hands (straight, straight flush)
   - Iterates through all possible combinations of future cards
   - Checks each for the desired hand
   - Calculates percentage of favorable outcomes

## Project Structure

```
Poker_Analytic/
├── app/
│   └── engine/
│       ├── base_odds.py          # Base class for calculators
│       ├── constants.py          # Constants (ranks, suits)
│       ├── state.py              # Game state
│       └── combinations/         # Hand calculators
│           ├── pair.py
│           ├── two_pair.py
│           ├── set.py
│           ├── straight.py
│           ├── flush.py
│           ├── full_hause.py
│           ├── kare.py
│           ├── street_flash.py
│           └── flush_royal.py
├── docs/
│   └── README.md
├── main.py                       # Usage example
└── test_all_combinations.py      # Tests
```

## Testing

Run tests to verify all calculators:

```bash
python test_all_combinations.py
```

## Calculation Examples

### Flush Draw on Flop
```python
game.set_hand(["Ah", "Kh"])
game.set_board(["Qh", "Jh", "2c"])
# Flush: ~35% (4 hearts, need 1 more from 9 remaining)
```

### Gutshot Straight Draw
```python
game.set_hand(["9h", "7d"])
game.set_board(["6c", "5h", "2c"])
# Straight: ~18% (need an eight, 4 outs)
```

### Set on Flop
```python
game.set_hand(["Ah", "Ad"])
game.set_board(["Ac", "Kh", "2c"])
# Set: 100% (already made)
# Full House: ~24% (need any pair)
# Kare: ~4% (need the last ace)
```

## Limitations

- Only Texas Hold'em is supported
- Other players' cards are not considered
- Straight calculation uses brute force (slower for large decks)

## License

MIT