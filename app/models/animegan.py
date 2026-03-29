
import torch
import cv2
from torchvision import transforms
from PIL import Image

# Load pretrained model (lightweight version)
model = torch.hub.load(
    "bryandlee/animegan2-pytorch:main",
    "generator",
    pretrained="face_paint_512_v2"
)

model.eval()

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

def animegan(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((512, 512))

    tensor = transform(img).unsqueeze(0)

    with torch.no_grad():
        output = model(tensor)[0]

    output = output.permute(1, 2, 0).numpy()
    output = ((output + 1) * 127.5).astype("uint8")

    return cv2.cvtColor(output, cv2.COLOR_RGB2BGR)