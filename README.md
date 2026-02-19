# 🧠 Handwritten Digit Recognition | Deep Learning Pipeline

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square) ![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python) ![TensorFlow](https://img.shields.io/badge/Framework-TensorFlow-orange?style=flat-square&logo=tensorflow) ![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-FF4B4B?style=flat-square&logo=streamlit)

An end-to-end Computer Vision application leveraging **Convolutional Neural Networks (CNN)** to perform real-time optical character recognition on handwritten digits. 

ጐ **Live Production Environment:** [Try the Demo](https://hand-written-digit-recognition-fdgurtwllfe6lizudj6eip.streamlit.app/)

---

## ፁ System Architecture

1.  **Preprocessing Layer**: Real-time image acquisition $\rightarrow$ Grayscale Conversion $\rightarrow$ Bitwise Inversion $\rightarrow$ Resizing ($28 \times 28$ pixels) $\rightarrow$ Normalization ($[0,1]$).
2.  **Model Layer**: Sequential CNN (Conv2D $\rightarrow$ MaxPool $\rightarrow$ Conv2D $\rightarrow$ MaxPool $\rightarrow$ Dense $\rightarrow$ Softmax).
3.  **Deployment Layer**: Served via Streamlit Community Cloud with CI/CD integration.

---

## ጐ Technical Challenges & Solutions

- **Inverted Polarity**: MNIST data uses white digits on black backgrounds, while user drawings are often black on white. 
  - *Solution*: Implemented a bitwise inversion (`255 - image`) in the preprocessing pipeline.
- **Model Latency**: Loading deep learning models on every request slows down UX.
  - *Solution*: Utilized Streamlit's `@st.cache_resource` to load the CNN model into memory once as a singleton.
- **Input Scaling**: Hand-drawn digits vary in thickness and position.
  - *Solution*: Used OpenCV interpolation (`INTER_AREA`) for high-quality resizing to $28 \times 28$ pixels.

---

## 🚀 Future Roadmap

- [ ] **Data Augmentation**: Incorporate rotation and shifting to improve model robustness.
- [ ] **Mobile Support**: Optimize the drawing canvas for touch-screen devices.
- [ ] **Multi-digit Recognition**: Extend the pipeline to recognize sequences of numbers using contour detection.

---

## ፃ Local Development Setup

```bash
git clone https://github.com/M-Divya29/Hand-Written-Digit-Recognition.git
cd Hand-Written-Digit-Recognition
pip install -r requirements.txt
streamlit run app.py
```

---

## ፁ Author
**Divya Lalitha** 
[ፃ GitHub](https://github.com/M-Divya29) | [ጐ Portfolio Site](https://github.com/M-Divya29/Hand-Written-Digit-Recognition)
