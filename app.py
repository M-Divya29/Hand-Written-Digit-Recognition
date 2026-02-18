import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.title("🧠 Handwritten Digit Recognition")

model = tf.keras.models.load_model("mnist_model.h5")

uploaded_file = st.file_uploader("Upload a digit image", type=["png", "jpg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L").resize((28,28))
    img_array = np.array(image)/255.0
    img_array = img_array.reshape(1,28,28)
    prediction = model.predict(img_array)
    st.write("Predicted Digit:", np.argmax(prediction))
