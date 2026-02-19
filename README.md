# ፃ Handwritten Digit Recognition using CNN

A real-time handwritten digit recognition web application built using a Convolutional Neural Network (CNN) trained on the MNIST dataset and deployed using Streamlit.

ጐ **Live App Link:** [Click here to try the app](https://hand-written-digit-recognition-fdgurtwllfe6lizudj6eip.streamlit.app/)

ፃ **GitHub Repository:** [https://github.com/M-Divya29/Hand-Written-Digit-Recognition](https://github.com/M-Divya29/Hand-Written-Digit-Recognition)

---

## ፃ Application Screenshots

| Drawing Canvas | Real-time Prediction |
|---|---|
| ![Canvas](screenshots/digit_7.png) | ![Prediction](screenshots/sample_output.png) |

---

## ጐ Features

- ✏️ **Interactive Canvas**: Draw digits (0-9) directly in your browser.
- ፁ **CNN Model**: High-accuracy deep learning model using TensorFlow/Keras (~98% accuracy).
- ፄ **Confidence Score**: Real-time prediction with probability percentage.
- ፂ **Preprocessing**: Automated image resizing, grayscale conversion, and color inversion.

---

## ፂ Tech Stack

- **Deep Learning**: TensorFlow, Keras
- **Web Framework**: Streamlit
- **Image Processing**: OpenCV, Pillow
- **Data Handling**: NumPy, Scikit-learn

---

## ፃ Project Structure

```text
Hand-Written-Digit-Recognition/
│
├── app.py              # Streamlit web application
├── digit_model.h5      # Trained CNN model
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── screenshots/        # App previews and sample digits
```

---

## ⚙️ Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/M-Divya29/Hand-Written-Digit-Recognition.git
   cd Hand-Written-Digit-Recognition
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

## ፁ Author
**Divya Lalitha**
[GitHub Profile](https://github.com/M-Divya29)
