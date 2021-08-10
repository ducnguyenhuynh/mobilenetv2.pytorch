import torch
import torch.nn as nn
import models.imagenet as customized_models 


num_classes = 7
model = customized_models.mobilenetv2(width_mult = 0.1)
model.load_state_dict(torch.load('pretrained/mobilenetv2_0.1-7d1d638a.pth'))
model.classifier = nn.Linear(model.output_channel, num_classes)
checkpoint = torch.load('savefiles_0.1/model_best.pth.tar')
model.load_state_dict(checkpoint['state_dict'])

