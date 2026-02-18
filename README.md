# 🧠 Handwritten Digit Recognition using CNN

A real-time handwritten digit recognition web application built using a Convolutional Neural Network (CNN) trained on the MNIST dataset and deployed using Streamlit. 

🔗 **GitHub Repository:** [https://github.com/M-Divya29/Hand-Written-Digit-Recognition](https://github.com/M-Divya29/Hand-Written-Digit-Recognition)

---

## 🚀 Features

- ✏️ **Interactive Canvas**: Draw digits (0-9) directly in your browser.
- 🤖 **CNN Model**: High-accuracy deep learning model using TensorFlow/Keras.
- 📊 **Confidence Score**: Real-time prediction with probability percentage.
- 🛠️ **Preprocessing**: Automated image resizing, grayscale conversion, and color inversion.

---

## 🛠 Tech Stack

- **Deep Learning**: TensorFlow, Keras
- **Web Framework**: Streamlit
- **Image Processing**: OpenCV, Pillow
- **Data Analysis**: NumPy, Scikit-learn

---

## 📂 Project Structure

```text
Hand-Written-Digit-Recognition/
│
├── app.py              # Streamlit web application
├── digit_model.h5      # Trained CNN model
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── screenshots/        # Sample digits and app previews
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

## 🧠 Model Architecture

The model is a Sequential CNN consisting of:
- **Conv2D Layer**: 32 filters, 3x3 kernel, ReLU activation.
- **MaxPooling Layer**: 2x2 pooling.
- **Conv2D Layer**: 64 filters, 3x3 kernel, ReLU activation.
- **Flatten Layer**: Converts 2D feature maps to 1D vector.
- **Dense Layer**: 64 neurons, ReLU activation.
- **Output Layer**: 10 neurons, Softmax activation.

---

## 👩‍💻 Author
**Divya Lalitha**  
[GitHub Profile](https://github.com/M-Divya29)
