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

## 🚀 Key Features

- ✏️ **Interactive Canvas**: Draw digits (0-9) directly in your browser with real-time feedback.
- 🤖 **CNN Model**: Advanced Deep Learning architecture (Conv2D, MaxPooling) achieving ~98% accuracy.
- 📊 **Confidence Score**: Dynamic probability display for the predicted digit.
- 🛠️ **Preprocessing Pipeline**: Automated resizing (28x28), grayscale conversion, and pixel normalization.

---

## 🛠 Tech Stack

- **Deep Learning**: TensorFlow, Keras
- **Frontend/Web**: Streamlit
- **Computer Vision**: OpenCV (cv2), Pillow
- **Mathematical Analysis**: NumPy
- **Model Training**: Scikit-learn

---

## 📂 Project Structure

```text
Hand-Written-Digit-Recognition/
│
├── app.py              # Main Streamlit application script
├── digit_model.h5      # Pre-trained CNN model weights
├── requirements.txt    # List of library dependencies
├── README.md           # Project documentation
└── screenshots/        # UI previews and dataset samples
```

---

## ⚙️ Local Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/M-Divya29/Hand-Written-Digit-Recognition.git
   cd Hand-Written-Digit-Recognition
   ```

2. **Setup Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

---

## 👩‍💻 Author
**Divya Lalitha**
[GitHub Profile](https://github.com/M-Divya29)
