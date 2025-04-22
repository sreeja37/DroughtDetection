# 🌾 Comparative Analysis of Drought Detection Using Satellite Imagery with Deep Learning Models 

![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

> An AI-powered tool to detect drought-prone areas using satellite imagery and deep learning models.

---

## 🔗 Live App

👉 [Click here to use the app](https://droughtdetection.streamlit.app/)

---

## 🧩 Project Development Process

### 📌 About the Project

Droughts impact agriculture, water resources, and rural livelihoods. This project provides a scalable solution using satellite imagery and deep learning for automated drought detection.

- Models used: **EfficientNetB0**, **MobileNetV2**, **VGG16**, and **Custom CNN**
- Classification is based on **cattle presence** (proxy indicator of vegetation and water availability)
- Web interface is built with **Streamlit**

---

### 📁 Dataset and Preprocessing

- Dataset Source: **W&B Drought Watch** (based on Landsat-8 RGB bands)
- Classes:
  - Class 0: 0 or 1 cow → Drought
  - Class 1: 2+ cows → No Drought
- Image Shape: 65×65×3 (RGB)
- Preprocessing:
  - Band selection (RGB), normalization
  - Augmentation (flip, rotate, brightness)
  - TFRecord conversion

---

### 🧠 Deep Learning Models

Trained and evaluated using standard metrics (Accuracy, Precision, Recall, F1-Score):

| Model          | Accuracy | Precision | Recall | F1-Score |
|----------------|----------|-----------|--------|----------|
| EfficientNetB0 | 90.31%   | 90.58%    | 90.31% | 90.30%   |
| MobileNetV2    | 84.21%   | 84.28%    | 84.21% | 84.24%   |
| VGG16          | 68.51%   | 69.61%    | 68.51% | 68.07%   |
| Custom CNN     | 78.59%   | 79.61%    | 79.59% | 79.60%   |

---

### 🖼️ Workflow

1. **Upload Satellite Image**
2. **Satellite Validator** checks image type
3. **Drought Detector** classifies drought status
4. **Visual Result & Recommendation** shown

---

### 📂 Project Structure

```
├── models/               # Trained .keras models
├── notebooks/            # Jupyter notebooks for training & evaluation
├── Streamlit.py          # Main Streamlit app
├── requirements.txt
└── README.md
```

---

## ⚙️ Execution Process

### 📦 Installation

```bash
git clone https://github.com/sreeja37/DroughtDetection.git
cd DroughtDetection
pip install -r requirements.txt
streamlit run Streamlit.py
```

- Ensure you place the `.keras` model files in the `models/` folder
- The app will prompt for a satellite image upload and analyze it in real time

---

### 🙌 Team

- Sreeja Pandraju  ~~ @sreeja37
- Adithya Manthena
- Swarupa Palaparthy
- Geetha Ramavath

---

### 📜 License

This project is open-sourced under the MIT License.
