
# 🔬 ViT Fingerprint Attention Visualizer

A lightweight project using **Vision Transformer (ViT)** to visualize attention maps on fingerprint images.  
This is a simplified version of a research-based fingerprint analysis system, ideal for showcasing ViT's ability to understand spatial patterns.

---

## 📌 Project Overview

This project uses a pretrained **ViT-Base** model to generate and visualize attention maps for a given fingerprint image.  
It highlights how different layers of the transformer **attend to various regions** of the input image.

- 🧠 Backbone: ViT-Base (from [timm](https://github.com/huggingface/pytorch-image-models))
- 📦 Input: Any image (preferably fingerprint)
- 🎯 Output: Attention heatmaps of the final transformer layer

---

## 🎯 Objectives

- Apply a **transformer-based model** to a vision task
- Understand **attention flow** from input image to classification head
- Create visual explanation maps for **model interpretability**

---

## 🚀 How to Run

1. Install required packages:
```bash
pip install torch torchvision timm matplotlib opencv-python pillow
```

2. Run the script:
```bash
python fingerprint_attention_vit.py
```

3. Select a fingerprint image when prompted (local file browser will appear).

---

## 📸 Sample Output

| Original Image | Attention Map |
|----------------|----------------|
| ![]Vision Transformer (ViT)/Dataset/Fake/clear silicone (1).bmp | ![](outputs\clear silicone (1)_attn.jpgattention_map_last_layer.jpg) |

> 🔍 These visualizations show which parts of the image the ViT model is focusing on when making predictions.

---

## 🗃️ Folder Structure

```
ViT-Fingerprint-Attention/
├── fingerprint_attention_vit.py
├── Outputs/
│   └── attention_map(1).png...
├── README.md
```

---

## 🧠 Background

This project is inspired by academic research on **transformer-based models for biometric analysis**, including fingerprint recognition and spoof detection.

---

## 📚 References

- [Timm – PyTorch Image Models](https://github.com/huggingface/pytorch-image-models)
- [ViT Paper – An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)

---
