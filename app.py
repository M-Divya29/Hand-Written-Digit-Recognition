import streamlit as st
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from PIL import Image

st.title("🧠 Handwritten Digit Recognition")

@st.cache_resource
def train_model():
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    X, y = mnist.data[:10000], mnist.target[:10000]  # Use 10k samples for faster training

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    return model, scaler

model, scaler = train_model()

uploaded_file = st.file_uploader("Upload a digit image (28x28 grayscale)", type=["png", "jpg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L").resize((28, 28))
    
    img_array = np.array(image)
    img_array = 255 - img_array   # 🔥 IMPORTANT: invert colors
    img_array = img_array.reshape(1, -1)
    img_array = scaler.transform(img_array)

    prediction = model.predict(img_array)
    st.write("### Predicted Digit:", prediction[0])
