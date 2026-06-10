import json
from pathlib import Path

import cv2
import numpy as np

import torch
from torchvision import transforms, models
import torch.nn as nn



def build_model():
    model = models.mobilenet_v3_small(weights=False)

    model.classifier[3] = nn.Linear(model.classifier[3].in_features, 52)

    return model



class PredictCard:

    def __init__(self):

        self.device = torch.device("cpu")

        self.model = build_model()

        mapping_path = Path(__file__).parent / "label_to_card.json"
        weights_path = Path(__file__).parent / "best_model2.pth"

        self.model.load_state_dict(
            torch.load(
                weights_path,
                map_location=self.device
            )
        )

        self.model = self.model.to(self.device)

        self.model.eval()

        self.transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

        with open(mapping_path, "r", encoding="utf-8") as f:
            self.idx = json.load(f)

    def preprocess_image(self, image: np.ndarray) -> torch.Tensor:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = self.transform(image)

        image = image.unsqueeze(0)

        return image

    def predict(self, image: np.ndarray) -> str:
        x = self.preprocess_image(image)

        x = x.to(self.device)

        with torch.no_grad():
            logits = self.model(x)

            pred_idx = torch.argmax(logits, dim=1).item()

            return self.idx[pred_idx]
