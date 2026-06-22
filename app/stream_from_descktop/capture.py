import dxcam
import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple, Generator
import logging

logger = logging.getLogger(__name__)


@dataclass
class CaptureConfig:
    fps: int = 30
    region: Optional[Tuple[int, int, int, int]] = None
    output_color: str = "RGB"


class ScreenCapture:

    def __init__(self, config: CaptureConfig = CaptureConfig()):
        self.config = config
        self._camera: Optional[dxcam.DXCamera] = None
        self._is_streaming = False

    def _get_camera(self) -> dxcam.DXCamera:
        if self._camera is None:
            self._camera = dxcam.create(output_color=self.config.output_color)
        return self._camera

    def grab_frame(self) -> Optional[np.ndarray]:
        camera = self._get_camera()
        frame = camera.grab(region=self.config.region)
        return frame

    def grab_frame_blocking(self) -> np.ndarray:
        while True:
            frame = self.grab_frame()
            if frame is not None:
                return frame

    def stream(self) -> Generator[np.ndarray, None, None]:

        camera = self._get_camera()
        camera.start(region=self.config.region, target_fps=self.config.fps)
        self._is_streaming = True
        logger.info(
            f"Stream started: {self.config.fps} FPS, region={self.config.region}"
        )

        try:
            while self._is_streaming:
                frame = camera.get_latest_frame()
                if frame is not None:
                    yield frame
        finally:
            camera.stop()
            self._is_streaming = False
            logger.info("Stream stopped")

    def stop(self):

        self._is_streaming = False

    def release(self):

        self.stop()
        if self._camera is not None:
            del self._camera
            self._camera = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.release()

    @staticmethod
    def get_screen_size() -> Tuple[int, int]:
        import ctypes

        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
