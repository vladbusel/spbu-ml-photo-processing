from base_model import ResNetUNet, device
import torch

num_class = 3

class NormModel(ResNetUNet):
    def __init__(self):
        super().__init__(num_class)
        self.to(device)
        self.load_state_dict(torch.load("norm_model/weight.pt", map_location=device))
        self.eval()
