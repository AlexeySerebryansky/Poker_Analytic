from pathlib import Path
import uuid

import cv2


class DatasetCollector:
    ALL_CARDS = [
        f"{rank}{suit}"
        for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        for suit in ["c", "d", "h", "s"]
    ]

    def __init__(self, dataset_dir: str = "dataset/Train"):

        self.dataset_dir = Path(__file__).parent / dataset_dir
        print(self.dataset_dir)

    def save(self, crop, label):
        save_dir = self.dataset_dir / label

        save_dir.mkdir(parents=True, exist_ok=True)

        file_path = save_dir / f"{uuid.uuid4().hex}.png"

        cv2.imwrite(str(file_path), crop)

        return file_path

    def get_stats(self):

        stats = {card: 0 for card in self.ALL_CARDS}

        for class_dir in self.dataset_dir.iterdir():

            if not class_dir.is_dir():
                continue

            stats[class_dir.name] = len(list(class_dir.glob("*.png")))

        return stats
