import keyboard

from calculating.odds_result import OddsCalculatorService
from classification.class_predictor import PredictCard
from engine.cards_grouper import CardGrouper
from engine.detection_matcher import RecognizedCard
from engine.state_builder import StateBuilder
from exeptions.duplicated_card_error import DuplicatedCardError
from stream_from_descktop.capture import ScreenCapture, CaptureConfig
from detection.detect_cards import DetectCards
from stream_from_descktop.frame_stability import CenterRegionFilter
from stream_from_descktop.windows_utils import WindowSelector

detect_cards = DetectCards()
predict_card = PredictCard()
frame_filter = CenterRegionFilter()
grouper = CardGrouper()
builder = StateBuilder()
calculator = OddsCalculatorService()

print("Select window with your game and press F8")

keyboard.wait("f8")

window = WindowSelector.select_window()

print(f"Selected{window.title}")

capture = ScreenCapture(
    CaptureConfig(
        fps=5, region=window.region
    )
)

for frame in capture.stream():

    if frame_filter.has_changed(frame):

        detections = detect_cards.detect_cards(frame)

        recognized_cards = []

        for detection in detections:
            crop = detection.crop(frame)

            card_name = predict_card.predict(crop)

            recognized_card = RecognizedCard(card=card_name, detection=detection)

            recognized_cards.append(recognized_card)

            print(f"Card name: {card_name}")

        try:

            grouped_cards = grouper.group(recognized_cards)

            state = builder.update(grouped_cards)

        except DuplicatedCardError as e:
            print(e)
            continue

        print(f"Hand: {state.hand}")
        print(f"Board: {state.board}")

        print("-----------")


        results = calculator.calculate(state)


        for combination, odds in results.items():
            print(f"Combination: {combination}  ---  {odds}")
