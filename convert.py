import torch
from torchvision.models import resnet50

model = resnet50()

model.load_state_dict(torch.load('edsr1_x4.pt', map_location=torch.device('cpu')))
model.eval()

dummy_input = torch.randn(1, 3, 496, 720)

torch.onnx.export(model, dummy_input, 'edsr1_x4.onnx', export_params=True)