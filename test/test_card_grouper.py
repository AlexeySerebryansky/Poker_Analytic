from engine.cards_grouper import CardGrouper
from engine.state_builder import StateBuilder
from engine.detection_matcher import RecognizedCard
from detection.detect_cards import DetectedCard

grouper = CardGrouper()
builder = StateBuilder()

cards = [
    RecognizedCard(
        card="Ah",
        detection=DetectedCard(x1=200, y1=500, x2=250, y2=550, confidence=0.9),
    ),
    RecognizedCard(
        card="7h",
        detection=DetectedCard(x1=200, y1=100, x2=250, y2=150, confidence=0.9),
    ),
    RecognizedCard(
        card="Ts",
        detection=DetectedCard(x1=300, y1=100, x2=350, y2=150, confidence=0.9),
    ),
    RecognizedCard(
        card="Kd",
        detection=DetectedCard(x1=300, y1=500, x2=350, y2=550, confidence=0.9),
    ),
    RecognizedCard(
        card="2c",
        detection=DetectedCard(x1=100, y1=100, x2=150, y2=150, confidence=0.9),
    ),
    RecognizedCard(
        card="Qd",
        detection=DetectedCard(x1=300, y1=500, x2=350, y2=550, confidence=0.9),
    ),
]

grouped = grouper.group(cards)

state = builder.update(grouped)

print(f"Hand: \n{state.hand}")
print(f"Board: \n{state.board}")
print(f"Street: {state.street}")
