import torch.nn as nn
from torchvision import models

class CardsClassifier(nn.Module):

    def __init__(self):
        super().__init__()

        self.model = models.mobilenet_v3_small(pretrained=True)

        in_features = self.model.classifier[3].in_features
        num_classes: int = 52

        self.model.classifier[3] = nn.Linear(
            in_features,
            num_classes
        )

    def forward(self, x):
        return self.model(x)