import keyboard

from helper_scripts.creater_dataset_classif.dataset_collector import DatasetCollector
from helper_scripts.creater_dataset_classif.main_window import MainWindow
from stream_from_descktop.capture import ScreenCapture, CaptureConfig
from detection.detect_cards import DetectCards
from stream_from_descktop.windows_utils import WindowSelector


print("Select window with your game and press F8")

keyboard.wait("f8")

window = WindowSelector.select_window()

capture = ScreenCapture(
    CaptureConfig(
        fps=5, region=window.region
    )
)

detector = DetectCards()

collector = DatasetCollector()

window = MainWindow(
    capture=capture,
    detector=detector,
    collector=collector
)


window.run()
