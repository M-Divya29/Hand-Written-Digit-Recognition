import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="Digit Recognition", page_icon="🧠")

st.title("🧠 Handwritten Digit Recognition using CNN")

@st.cache_resource
def load_or_train_model():
    try:
        model = tf.keras.models.load_model("digit_model.h5")
        return model
    except:
        from sklearn.datasets import fetch_openml
        mnist = fetch_openml('mnist_784', version=1, as_frame=False)

        X = mnist.data.reshape(-1, 28, 28, 1).astype("float32") / 255.0
        y = mnist.target.astype("int")

        model = models.Sequential([
            layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
            layers.MaxPooling2D((2,2)),
            layers.Conv2D(64, (3,3), activation='relu'),
            layers.MaxPooling2D((2,2)),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(X, y, epochs=3, batch_size=128, verbose=0)

        model.save("digit_model.h5")
        return model

model = load_or_train_model()

st.write("Draw a digit (0–9) below:")

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=18,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:

    img = canvas_result.image_data
    img = cv2.cvtColor(img.astype('uint8'), cv2.COLOR_BGR2GRAY)

    if np.mean(img) > 250:
        st.info("Draw a digit first ✏️")
    else:
        img = cv2.resize(img, (28, 28))
        img = 255 - img
        img = img.astype("float32") / 255.0
        img = img.reshape(1, 28, 28, 1)

        prediction = model.predict(img)
        digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.subheader(f"Predicted Digit: {digit}")
        st.write(f"Confidence: {confidence:.2f}%")
