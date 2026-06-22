from pathlib import Path
from ultralytics import YOLO
from dataclasses import dataclass
from typing import List
import numpy as np


@dataclass
class DetectedCard:
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float

    def crop(self, frame: np.ndarray) -> np.ndarray:
        return frame[self.y1 : self.y2, self.x1 : self.x2]

    @property
    def center_y(self) -> float:
        return (self.y1 + self.y2) // 2


class DetectCards:

    def __init__(self, confidence_threshold: float = 0.5):
        model_path = Path(__file__).parent / "card_detect.pt"
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold

    def detect_cards(self, frame) -> List[DetectedCard]:
        results = self.model.predict(
            source=frame, conf=self.confidence_threshold, verbose=False
        )

        detections = []

        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            detections.append(
                DetectedCard(
                    x1=int(x1),
                    y1=int(y1),
                    x2=int(x2),
                    y2=int(y2),
                    confidence=float(box.conf[0]),
                )
            )

        return detections
