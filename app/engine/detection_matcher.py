from dataclasses import dataclass

from detection.detect_cards import DetectedCard


@dataclass(frozen=True)
class RecognizedCard:

    card: str

    detection: DetectedCard