# ፁ Handwritten Digit Recognition | Deep Learning Pipeline

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=flat-square) ![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python) ![TensorFlow](https://img.shields.io/badge/Framework-TensorFlow-orange?style=flat-square&logo=tensorflow) ![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-FF4B4B?style=flat-square&logo=streamlit)

An end-to-end Computer Vision application leveraging **Convolutional Neural Networks (CNN)** to perform real-time optical character recognition on handwritten digits. This project demonstrates the integration of deep learning models with responsive web interfaces for interactive inference.

ጐ **Live Production Environment:** [Try the Demo](https://hand-written-digit-recognition-fdgurtwllfe6lizudj6eip.streamlit.app/)

---

## ፁ System Architecture

The application follows a decoupled architecture separating the inference engine from the presentation layer:

1.  **Preprocessing Layer**: Real-time image acquisition -> Grayscale Conversion -> Bitwise Inversion -> Resizing (28x28 pixels) -> Normalization ([0,1]).
2.  **Model Layer**: A sequential CNN architecture utilizing Conv2D layers for spatial feature extraction and Dense layers for categorical classification.
3.  **Deployment Layer**: Served via Streamlit Community Cloud with CI/CD integration for seamless updates.

---

## ጐ Technical Features

- **Robust Inference Engine**: Powered by a CNN model trained on the MNIST dataset, achieving a validation accuracy of **~98%**.
- **Interactive UX**: Custom-built drawing canvas using `streamlit-drawable-canvas` for fluid user interaction.
- **Optimized Performance**: Singleton model loading using `@st.cache_resource` to minimize memory overhead and latency.

---

## ፁ Repository Structure

```text
Hand-Written-Digit-Recognition/
┣━━ app.py               # Application entry point & UI logic
┣━━ digit_model.h5       # Pre-trained CNN weights
┣━━ requirements.txt     # Dependency manifest
┣━━ README.md            # Technical documentation
┗━━ screenshots/         # Asset directory
```

---

## ፁ Local Development Setup

### Prerequisites
- Python 3.9+
- Virtual Environment tool

### Installation
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/M-Divya29/Hand-Written-Digit-Recognition.git
    cd Hand-Written-Digit-Recognition
    ```
2.  **Environment Configuration**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Application**
    ```bash
    streamlit run app.py
    ```

---

## ፁ Author
**Divya Lalitha**
[GitHub](https://github.com/M-Divya29)
