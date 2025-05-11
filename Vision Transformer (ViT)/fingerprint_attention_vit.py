import os
import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.utils import save_image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
from timm import create_model
from torchvision.transforms.functional import to_pil_image

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# ---------------------
# Setup
# ---------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
image_size = 224
model_path = "vit_fingerprint_classifier.pth"
image_folder = "dataset"  # Contains live/ and fake/ folders

# ---------------------
# Preprocessing
# ---------------------
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])

# ---------------------
# Load Model
# ---------------------
model = create_model('vit_base_patch16_224', pretrained=False, num_classes=2)
model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()
model.to(device)

# ---------------------
# Hook for Attention
# ---------------------
attn_weights = []

def get_attention_hook(module, input, output):
    attn = module.get_attn() if hasattr(module, 'get_attn') else module.attn_drop(output)
    attn_weights.append(attn.detach().cpu())

handle = model.blocks[-1].attn.register_forward_hook(get_attention_hook)

# ---------------------
# Attention Visualization
# ---------------------
def visualize_attention(img_tensor, attn_map, output_path, img_path):
    import matplotlib.pyplot as plt
    import cv2
    from torchvision.transforms.functional import to_pil_image

    print("attn_map shape:", attn_map.shape)  # Debug

    if attn_map.ndim == 3:  # [num_heads, num_tokens, num_tokens]
        attn_map = attn_map.mean(0)[0, 1:]  # Avg heads → [num_tokens, num_tokens] → [CLS to patches]
    elif attn_map.ndim == 2:  # [num_tokens, num_tokens]
        attn_map = attn_map[0, 1:]
    elif attn_map.ndim == 1:  # Already 1D
        attn_map = attn_map[1:]
    else:
        raise ValueError("Unsupported attention shape")

    num_patches = attn_map.shape[0]
    map_size = int(np.sqrt(num_patches))
    attn_map = attn_map[:map_size**2].reshape(map_size, map_size).cpu().numpy()
    attn_map = cv2.resize(attn_map, (img_tensor.shape[-1], img_tensor.shape[-2]))

    attn_map = (attn_map - attn_map.min()) / (attn_map.max() - attn_map.min() + 1e-6)
    img = to_pil_image(img_tensor.squeeze(0).cpu())

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img)
    axs[0].set_title("Original Image")
    axs[0].axis('off')
    axs[1].imshow(img)
    axs[1].imshow(attn_map, cmap='jet', alpha=0.5)
    axs[1].set_title("Attention Map")
    axs[1].axis('off')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    # Optional: display saved attention overlay
    original = cv2.imread(img_path)
    original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    overlay = cv2.imread(output_path)
    overlay = cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(overlay)
    plt.title("Attention Overlay")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# ---------------------
# Inference on All Images
# ---------------------
class_map = {0: "live", 1: "fake"}
results_dir = "outputs"
os.makedirs(results_dir, exist_ok=True)

for label in os.listdir(image_folder):
    subfolder = os.path.join(image_folder, label)
    for filename in os.listdir(subfolder):
        if not filename.lower().endswith(".bmp"):
            continue

        image_path = os.path.join(subfolder, filename)
        image = Image.open(image_path).convert("RGB")
        img_tensor = transform(image).unsqueeze(0).to(device)

        attn_weights.clear()
        with torch.no_grad():
            output = model(img_tensor)
            pred = torch.argmax(output, dim=1).item()

        predicted_label = class_map[pred]
        print(f"{filename} => Predicted: {predicted_label}")

        output_file = os.path.join(results_dir, f"{os.path.splitext(filename)[0]}_attn.jpg")
        visualize_attention(img_tensor, attn_weights[0], output_file, image_path)

handle.remove()
