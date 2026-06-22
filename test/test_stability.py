import cv2
import keyboard

from stream_from_descktop.capture import ScreenCapture, CaptureConfig
from stream_from_descktop.windows_utils import WindowSelector
from stream_from_descktop.frame_stability import CenterRegionFilter

print("Select window with your game and press F8")

keyboard.wait("f8")

window = WindowSelector.select_window()

print(f"Selected{window.title}")

capture = ScreenCapture(
    CaptureConfig(
        fps=30, region=window.region
    )
)

frame_filter = CenterRegionFilter()

for frame in capture.stream():
    if frame_filter.has_changed(frame):
        debug_frame = frame_filter.draw_debug(frame)

        cv2.imshow(
            "debug",
            debug_frame
        )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
