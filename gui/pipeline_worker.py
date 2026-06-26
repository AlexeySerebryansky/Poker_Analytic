from pathlib import Path
from PyQt6.QtCore import QThread, pyqtSignal

from calculating.odds_result import OddsCalculatorService
from classification.class_predictor import PredictCard
from detection.detect_cards import DetectCards
from engine.cards_grouper import CardGrouper
from engine.detection_matcher import RecognizedCard
from engine.state_builder import StateBuilder
from stream_from_descktop.frame_stability import CenterRegionFilter
from exeptions.duplicated_card_error import DuplicatedCardError


class PipelineWorker(QThread):
    state_updated = pyqtSignal(object, dict)
    status_updated = pyqtSignal(str)
    error_updated = pyqtSignal(str)
    log_updated = pyqtSignal(str)

    LOG_FILE = Path(__file__).parent / "log.txt"

    def __init__(self, window, streamer):
        super().__init__()

        self.detect_cards = DetectCards()
        self.predict_card = PredictCard()
        self.frame_filter = CenterRegionFilter()
        self.grouper = CardGrouper()
        self.builder = StateBuilder()
        self.calculator = OddsCalculatorService()
        self.window = window
        self.streamer = streamer
        self.last_frame_number = -1

        self.running = True

    def run(self):

        self.log("starting pipeline")

        while self.running:

            frame = self.streamer.latest_frame

            if frame is None:
                QThread.msleep(1)
                continue

            if self.streamer.frame_number == self.last_frame_number:
                QThread.msleep(1)
                continue

            self.last_frame_number = self.streamer.frame_number

            try:

                x1, y1, x2, y2 = self.window.region

                frame = frame[y1:y2, x1:x2]

                if not self.running:
                    break

                if not self.frame_filter.has_changed(frame):
                    continue

                self.log("Frame updated")

                detections = self.detect_cards.detect_cards(frame)

                self.log(f"Detected cards{len(detections)}")

                recognized_cards = []

                for detection in detections:
                    crop = detection.crop(frame)

                    card_name = self.predict_card.predict(crop)

                    recognized_cards.append(
                        RecognizedCard(card=card_name, detection=detection)
                    )

                grouped_cards = self.grouper.group(recognized_cards)

                self.log("Group updated")

                state = self.builder.update(grouped_cards)

                self.log(f"Hand={state.hand}, Board={state.board}")

                try:
                    odds = self.calculator.calculate(state)

                except DuplicatedCardError as e:

                    self.log(f"Duplicated card: {e}")

                    self.error_updated.emit(str(e))
                    continue

                self.log("Odds calculated")

                self.state_updated.emit(state, odds)

                self.log("state updated")

            except Exception as e:
                self.log(f"Frame processing: {e}")
                continue

    def log(self, message: str):
        self.log_updated.emit(message)

        with self.LOG_FILE.open("a", encoding="utf-8") as f:
            f.write(f"{message}\n")
