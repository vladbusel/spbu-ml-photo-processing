from depth_model.depth_model import DepthModel
from mask_model.mask_model import MaskModel
from norm_model.norm_model import NormModel
from blender_handler.blender_handler import BlenderHandler
from torchvision import transforms
import torch
from PIL import Image
from base_model import device
import os
import torch.nn as nn
import numpy as np


class PhotoProcessingService():
    def __init__(self):
        pass

    def call(self, photo, params):
        photo = Image.open(photo)

        trans = transforms.Compose([
            transforms.Resize((256,256)),
            transforms.ToTensor()
        ])
        # photo = rgba2rgb(photo)
        photo = trans(photo)
        photo = torch.unsqueeze(photo, 0)
        photo = photo.to(device)

        mask_model = MaskModel()
        mask = mask_model.forward(photo)[0]
        mask = (mask>0.35).float()

        photo_front = photo[0] * mask
        photo_front = torch.unsqueeze(photo_front, 0)

        depth_model = DepthModel()
        depth = depth_model.forward(photo_front)[0]
        norm_model = NormModel()
        norm = norm_model.forward(photo_front)[0]

        depth = depth * mask

        norm = torch.cat([norm, torch.ones(1, 256, 256).to(device)])
        norm = norm * mask

        depth = transforms.ToPILImage()(depth)
        depth.save('depth.png')
        norm = transforms.ToPILImage()(norm)
        norm.save('norm.png')

        BlenderHandler().call(params)

        return "result.png"
