# 🌾 Comparative Analysis of Drought Detection Using Satellite Imagery with Deep Learning Models

An AI-powered tool to detect drought-prone areas using satellite imagery and deep learning models.

![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-green)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

### 🔗 Live Demo

👉 **[Click here to use the app](https://droughtdetection.streamlit.app/)**

---

## 🧩 Project Development Process

### 📌 About the Project

Droughts severely impact agriculture, water resources, and local livelihoods. This project aims to provide a scalable, automated drought detection system using satellite imagery and deep learning.

- **Models used**: EfficientNetB0, MobileNetV2, VGG16, and a custom CNN  
- **Classification basis**: Cattle presence (as a proxy for vegetation and water)  
- **Frontend**: Built with Streamlit for user-friendly interaction  

---

### 📁 Dataset and Preprocessing

- **Source**: W&B Drought Watch Dataset (Landsat-8 RGB bands)  
- **Image Size**: 65×65×3  

**Classes**:  
- Class 0: 0 or 1 cow → *Drought*  
- Class 1: 2 or more cows → *No Drought*  

**Preprocessing Includes**:
- RGB band extraction and normalization  
- Data augmentation (flip, rotate, brightness changes)  
- TFRecord conversion for model training  

---

### 🧠 Deep Learning Models

All models were evaluated using standard classification metrics:

| Model          | Accuracy | Precision | Recall | F1-Score |
|----------------|----------|-----------|--------|----------|
| EfficientNetB0 | 90.31%   | 90.58%    | 90.31% | 90.30%   |
| MobileNetV2    | 84.21%   | 84.28%    | 84.21% | 84.24%   |
| VGG16          | 68.51%   | 69.61%    | 68.51% | 68.07%   |
| Custom CNN     | 78.59%   | 79.61%    | 79.59% | 79.60%   |

---

### 🖼️ Workflow Overview

1. Upload satellite image  
2. Satellite validator checks if image is valid  
3. Drought detection model analyzes the image  
4. Results and recommendations are displayed visually  

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

### 📦 Installation Instructions

```bash
git clone https://github.com/sreeja37/DroughtDetection.git
cd DroughtDetection
pip install -r requirements.txt
streamlit run Streamlit.py
```

- Place the trained `.keras` models into the `models/` directory.  
- The app will prompt for an image upload and perform drought analysis in real time.

---

## 🙌 Team

- **Sreeja Pandraju** – [@sreeja37](https://github.com/sreeja37)  
- Adithya Manthena  
- Swarupa Palaparthy  
- Geetha Ramavath  

---

## 📜 License

This project is licensed under the [MIT License](https://github.com/sreeja37/DroughtDetection/blob/main/LICENSE).
