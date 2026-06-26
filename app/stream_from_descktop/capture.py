import dxcam
import numpy as np
from typing import Optional


class ScreenStreamer:

    def __init__(self, fps: int = 30, output_color: str = "RGB"):
        self.fps = fps
        self.output_color = output_color

        self.camera = dxcam.create(
            output_color=output_color
        )

        self.latest_frame: Optional[np.ndarray] = None

        self.frame_number = 0

    def start(self):
        self.camera.start(
            target_fps=self.fps
        )

    def update(self):
        frame = self.camera.get_latest_frame()

        if frame is not None:
            self.latest_frame = frame
            self.frame_number += 1

        return frame

    def stop(self):
        self.camera.stop()
