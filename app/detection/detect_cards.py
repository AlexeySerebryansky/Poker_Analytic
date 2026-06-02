from pathlib import Path
from ultralytics import YOLO
from dataclasses import dataclass
from typing import List


@dataclass
class Detection:
    x1: int
    y1: int
    x2: int
    y2: int
    confidence: float


class DetectCards:

    def __init__(self, confidence_threshold: float = 0.5):
        model_path = Path(__file__).parent / "detect_cards_model.pt"
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold

    def detect_cards(self, frame) -> List[Detection]:
        results = self.model.predict(
            source = frame,
            conf = self.confidence_threshold,
            verbose = False
        )

        detections = []

        for box in results[0].boxes:

            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

            detections.append(Detection(
                x1 = int(x1),
                y1 = int(y1),
                x2 = int(x2),
                y2 = int(y2),
                confidence = float(box.conf[0])
            ))

        return detections



