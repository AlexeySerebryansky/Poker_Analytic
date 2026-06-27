import traceback
from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal

from calculating.odds_result import OddsCalculatorService
from classification.class_predictor import PredictCard
from detection.detect_cards import DetectCards
from engine.cards_grouper import CardGrouper
from engine.detection_matcher import RecognizedCard
from engine.state import GameState
from engine.state_builder import StateBuilder
from exeptions.game_state_error import GameStateError
from stream_from_descktop.frame_stability import CenterRegionFilter


class PipelineWorker(QThread):
    state_updated = pyqtSignal(object, object)
    status_updated = pyqtSignal(str)
    error_updated = pyqtSignal(str)
    log_updated = pyqtSignal(str)

    LOG_FILE = Path(__file__).parent / "log.txt"

    def __init__(self, window, capture):
        super().__init__()

        self.detect_cards = DetectCards()
        self.predict_card = PredictCard()
        self.frame_filter = CenterRegionFilter()
        self.grouper = CardGrouper()
        self.builder = StateBuilder()
        self.calculator = OddsCalculatorService()
        self.window = window
        self.capture = capture

        self.running = True

    def run(self):

        self.log("starting pipeline")

        last_frame = -1

        while self.running:

            if self.capture.frame_number == last_frame:
                QThread.msleep(1)
                continue

            last_frame = self.capture.frame_number

            frame = self.capture.latest_frame

            if frame is None:
                continue

            frame = frame.copy()

            x1, y1, x2, y2 = self.window.region

            frame = frame[y1:y2, x1:x2]

            try:
                if not self.running:
                    break

                if not self.frame_filter.has_changed(frame):
                    continue

                self.log("Frame updated")

                detections = self.detect_cards.detect_cards(frame)

                self.log(f"Detected cards {len(detections)}")
                self.status_updated.emit(f"Detected cards: {len(detections)}")

                recognized_cards = []

                for detection in detections:
                    crop = detection.crop(frame)

                    self.log(
                        f"Crop: {crop.shape} "
                        f"({detection.x1}, {detection.y1}) "
                        f"({detection.x2}, {detection.y2})"
                    )

                    if crop.size == 0:
                        self.log("EMPTY CROP")
                        continue

                    card_name = self.predict_card.predict(crop)

                    recognized_cards.append(
                        RecognizedCard(card=card_name, detection=detection)
                    )

                grouped_cards = self.grouper.group(recognized_cards)

                self.log("Group updated")

                try:

                    state = self.builder.build(grouped_cards)

                    self.log(f"Hand={state.hand}, Board={state.board}")


                except GameStateError as e:

                    self.status_updated.emit(e.user_message)
                    self.error_updated.emit(e)
                    self.state_updated.emit(GameState(), None)

                    self.log(f"Game state error: {e}")

                    continue

                odds = self.calculator.calculate(state)

                self.log("Odds calculated")

                self.state_updated.emit(state, odds)

                self.log("state updated")

            except Exception:
                self.log(traceback.format_exc())
                continue

    def log(self, message: str):
        self.log_updated.emit(message)

        with self.LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"{message}\n")
