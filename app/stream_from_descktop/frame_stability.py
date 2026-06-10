import cv2
import numpy as np


class CenterRegionFilter:

    def __init__(self,
                 width_ratio: float = 0.45,
                 height_ratio: float = 0.12,
                 pixel_threshold: int = 20,
                 change_ratio_threshold: float = 0.01,
                 ):
        self.width_ratio = width_ratio
        self.height_ratio = height_ratio

        self.pixel_threshold = pixel_threshold
        self.change_ratio_threshold = change_ratio_threshold

        self._previous_roi = None

    def has_changed(self, frame: np.ndarray) -> bool:
        roi = self._extract_roi(frame)
        roi = self._preprocess(roi)

        if self._previous_roi is None:
            self._previous_roi = roi
            return True

        diff = cv2.absdiff(self._previous_roi, roi)

        changed_pixels = np.count_nonzero(diff > self.pixel_threshold)

        change_ratio = (changed_pixels / diff.size)

        if change_ratio >= self.change_ratio_threshold:
            self._previous_roi = roi
            return True

        return False

    def _extract_roi(self, frame: np.ndarray) -> np.ndarray:

        height, width = frame.shape[:2]

        center_x = width // 2
        center_y = height // 2

        roi_width = int(width * self.width_ratio)

        roi_height = int(height * self.height_ratio)

        x1 = center_x - roi_width // 2
        x2 = center_x + roi_width // 2

        y1 = center_y - roi_height // 2
        y2 = center_y + roi_height // 2

        return frame[y1:y2, x1:x2]

    @staticmethod
    def _preprocess(roi: np.ndarray) -> np.ndarray:

        gray = cv2.cvtColor(
            roi,
            cv2.COLOR_BGR2GRAY
        )

        return cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

    def draw_debug(self, frame: np.ndarray) -> np.ndarray:

        debug_frame = frame.copy()

        height, width = frame.shape[:2]

        center_x = width // 2
        center_y = height // 2

        roi_width = int(
            width * self.width_ratio
        )

        roi_height = int(
            height * self.height_ratio
        )

        x1 = center_x - roi_width // 2
        y1 = center_y - roi_height // 2

        x2 = center_x + roi_width // 2
        y2 = center_y + roi_height // 2

        cv2.rectangle(
            debug_frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.circle(
            debug_frame,
            (center_x, center_y),
            3,
            (0, 0, 255),
            -1
        )

        return debug_frame
