import keyboard

from classification.class_predictor import PredictCard
from stream_from_descktop.capture import ScreenCapture, CaptureConfig
from detection.detect_cards import DetectCards
from stream_from_descktop.frame_stability import CenterRegionFilter
from stream_from_descktop.windows_utils import WindowSelector


def main():
    detect_cards = DetectCards()
    predict_card = PredictCard()
    frame_filter = CenterRegionFilter()

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

            for detection in detections:
                crop = detection.crop(frame)

                card_name = predict_card.predict(crop)

                print(f"Card name: {card_name}")


if __name__ == '__main__':
    main()
