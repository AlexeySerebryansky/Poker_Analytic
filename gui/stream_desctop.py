from PyQt6.QtCore import QThread

from stream_from_descktop.capture import ScreenCapture


class CaptureThread(QThread):

    def __init__(self, capture: ScreenCapture):
        super().__init__()
        self.capture = capture

        self.latest_frame = None
        self.frame_number = 0
        self.running = True

    def run(self):

        for frame in self.capture.stream():

            if not self.running:
                break

            self.latest_frame = frame
            self.frame_number += 1


    def stop(self):
        self.running = False
        self.capture.stop()