# 🧠 Handwritten Digit Recognition using CNN

A real-time handwritten digit recognition web application built using a Convolutional Neural Network (CNN) trained on the MNIST dataset and deployed using Streamlit.

🚀 **Live App Link:** [Click here to try the app](https://unbalkingly-postlicentiate-willette.ngrok-free.dev/)

🔗 **GitHub Repository:** [https://github.com/M-Divya29/Hand-Written-Digit-Recognition](https://github.com/M-Divya29/Hand-Written-Digit-Recognition)

---

## 📸 Application Screenshots

| Drawing Canvas | Real-time Prediction |
|---|---|
| ![Canvas](screenshots/sample_output.png) | ![Prediction](screenshots/digit_7.png) |

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
- **Tunneling**: Pyngrok (for public access from Colab)

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

## 🌐 Deployment Details

- **Environment**: Developed in Google Colab.
- **Hosting**: Streamlit was exposed to the public internet using **ngrok**.
- **Production**: For permanent hosting, this project is ready to be deployed on **Streamlit Community Cloud** by connecting this GitHub repository.

---

## 👩‍💻 Author
**Divya Lalitha**  
[GitHub Profile](https://github.com/M-Divya29)
