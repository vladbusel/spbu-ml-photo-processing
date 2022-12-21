from base_model import ResNetUNet, device
import torch

num_class = 1

class MaskModel(ResNetUNet):
    def __init__(self):
        super().__init__(num_class)
        self.to(device)
        self.load_state_dict(torch.load("mask_model/weight.pt", map_location=device))
        self.eval()
