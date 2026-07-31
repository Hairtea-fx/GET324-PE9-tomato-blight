import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load the trained model
import os
MODEL_PATH = os.path.join(os.path.dirname(__file__), "tomato_blight_model.keras")
model = tf.keras.models.load_model(MODEL_PATH)

class_names = ['Tomato Early Blight', 'Tomato Late Blight']

st.title("🍅 Tomato Blight Classifier")
st.write("Upload a tomato leaf image to check whether it shows Early Blight or Late Blight.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0][0]
    predicted_class = class_names[1] if prediction > 0.5 else class_names[0]
    confidence = prediction if prediction > 0.5 else 1 - prediction

    st.subheader(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence*100:.2f}%")