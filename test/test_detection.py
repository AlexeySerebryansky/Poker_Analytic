import keyboard
import cv2

from stream_from_descktop.capture import ScreenCapture, CaptureConfig
from detection.detect_cards import DetectCards
from stream_from_descktop.windows_utils import WindowSelector

model = DetectCards()

print("Select window with your game and press F8")

keyboard.wait("f8")

window = WindowSelector.select_window()

print(f"Selected{window.title}")

capture = ScreenCapture(CaptureConfig(fps=5, region=window.region))

for frame in capture.stream():
    detections = model.detect_cards(frame)

    draw_frame = frame.copy()

    for detection in detections:
        cv2.rectangle(
            draw_frame,
            (detection.x1, detection.y1),
            (detection.x2, detection.y2),
            (0, 255, 0),
            2,
        )

        cv2.putText(
            draw_frame,
            f"{detection.confidence:.2f}",
            (detection.x1, detection.y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )

    cv2.imshow("Detections", cv2.cvtColor(draw_frame, cv2.COLOR_RGB2BGR))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
