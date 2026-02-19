# 🧠 Handwritten Digit Recognition using CNN

A real-time handwritten digit recognition web application built using a Convolutional Neural Network (CNN) trained on the MNIST dataset and deployed using Streamlit.

🚀 **Live App Link:** [Click here to try the app](https://hand-written-digit-recognition-fdgurtwllfe6lizudj6eip.streamlit.app/)

🔗 **GitHub Repository:** [https://github.com/M-Divya29/Hand-Written-Digit-Recognition](https://github.com/M-Divya29/Hand-Written-Digit-Recognition)

---

## 📸 Sample Digits from Dataset

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| ![](screenshots/digit_0.png) | ![](screenshots/digit_1.png) | ![](screenshots/digit_2.png) | ![](screenshots/digit_3.png) | ![](screenshots/digit_4.png) |

| 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|
| ![](screenshots/digit_5.png) | ![](screenshots/digit_6.png) | ![](screenshots/digit_7.png) | ![](screenshots/digit_8.png) | ![](screenshots/digit_9.png) |

---

## 🚀 Features

- ✏️ **Interactive Canvas**: Draw digits (0-9) directly in your browser.
- 🤖 **CNN Model**: High-accuracy deep learning model using TensorFlow/Keras (~98% accuracy).
- 📊 **Confidence Score**: Real-time prediction with probability percentage.
- 🛠️ **Preprocessing**: Automated image resizing, grayscale conversion, and color inversion.

---

## 🛠 Tech Stack

- **Deep Learning**: TensorFlow, Keras
- **Web Framework**: Streamlit
- **Image Processing**: OpenCV, Pillow

---

## 📂 Project Structure

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

## 👩‍💻 Author
**Divya Lalitha**
[GitHub Profile](https://github.com/M-Divya29)
