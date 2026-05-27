import json
from PIL import Image

import torch
from torchvision import transforms

from classification.model import CardsClassifier


class Predictor:

    def __init__(self, weights_path: str, mapping_path:str,  device: str = "cpu"):

        self.device = torch.device(device)

        self.model = CardsClassifier()

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

    def preprocess_image(self, image_path: str) -> torch.Tensor:

        image = Image.open(image_path).convert("RGB")

        image = self.transform(image)

        image = image.unsqueeze(0)

        return image


    def predict(self, image_path: str) -> str:

        x = self.preprocess_image(image_path)

        x = x.to(self.device)

        with torch.no_grad():

            logits = self.model(x)

            probs = torch.softmax(logits, dim=1)

            pred_idx = torch.argmax(probs, dim=1)

            pred_class = self.idx[str(pred_idx)]

            return pred_class.item()