from PyQt6.QtCore import QThread


class CaptureWorker(QThread):

    def __init__(self, streamer):
        super().__init__()

        self.streamer = streamer
        self.running = True

    def run(self):
        self.streamer.start()

        while self.running:

            frame = self.streamer.update()

            if frame is not None:
                print(id(frame))

            QThread.msleep(1)

        self.streamer.stop()

    def stop(self):
        self.running = False
