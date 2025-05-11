# 🦠 Malaria Detection Using CNN & Transfer Learning (VGG19)

![malaria-banner](https://user-images.githubusercontent.com/placeholder/malaria.jpg)

## 🚀 Overview

Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. Early and accurate detection is crucial for effective treatment and control. This project leverages **Convolutional Neural Networks (CNNs)** and **Transfer Learning with VGG19** to build a deep learning model that classifies cell images as **infected** or **uninfected** by malaria parasites.

## 📌 Project Highlights

* 🧠 **Two Approaches**:

  * Custom CNN from scratch
  * Transfer learning using **VGG19** pretrained on ImageNet
* 📂 Image classification on blood smear microscopy images
* 🧪 Achieved high validation accuracy and minimal loss
* 📊 Visualizations for training/validation accuracy & loss
* 💾 Saved trained model for future use and deployment

---

## 🧰 Technologies & Libraries

* Python
* TensorFlow / Keras
* NumPy, Matplotlib
* VGG19 (Transfer Learning)
* ImageDataGenerator (for preprocessing & augmentation)

---

## 📁 Dataset

* Source: [NIH Malaria Dataset](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria)
* Structure:

  ```
  Dataset/
  ├── Train/
  │   ├── Parasitized/
  │   └── Uninfected/
  └── Test/
      ├── Parasitized/
      └── Uninfected/
  ```

---

## 🧪 Model Architecture

### 🔬 1. Transfer Learning (VGG19)

* Feature extractor from **VGG19**
* Fully connected layers for classification
* All convolutional layers frozen during training

### 🧱 2. Custom CNN

* 3 convolutional + max pooling blocks
* Dense layers with softmax activation
* Built from scratch to compare with VGG19 performance

---

## 📈 Training Results

* 100 Epochs
* Accuracy: \~95%+
* Loss curves and accuracy plotted for comparison

<div align="center">
  <img src="images/loss_curve.png" width="400"/>
  <img src="images/acc_curve.png" width="400"/>
</div>

---

## 🧪 How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/malaria-detection-cnn-vgg19.git
   cd malaria-detection-cnn-vgg19
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (optional if you want to retrain):

   ```python
   python train_model.py
   ```

4. Make predictions on new images:

   ```python
   python predict.py --image path_to_image
   ```

---

## 🧠 Prediction Example

```python
img = image.load_img('Dataset/Test/Parasite/3.png', target_size=(224, 224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)
print("Infected" if np.argmax(prediction) == 0 else "Uninfected")
```

---

## 📌 Results

* ✅ Successfully detects malaria-infected cells
* 🧪 Transfer learning (VGG19) outperforms custom CNN
* 💡 Easy to extend for mobile or web-based deployment

---

## 📬 Future Improvements

* 📲 Deploy as a web or mobile app
* 🩺 Add explainability (Grad-CAM, attention)
* 🔄 Fine-tune VGG19 for improved performance

