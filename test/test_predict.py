import torch

state_dict = torch.load("app/classification/best_model2.pth")

for key in list(state_dict.keys())[:30]:
    print(key)
