
import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from PIL import Image
import tempfile

def load_and_preprocess_for_satellite(image_path, target_size=(64, 64)):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def load_and_preprocess_for_drought(image_path, target_size=(65, 65)):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

st.title("🌍 Satellite Image Drought Detection")
st.markdown("Upload a satellite image for analysis")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=300)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    try:
        sat_model = tf.keras.models.load_model("D:\project\satellite_classifier_finetuned_v2.keras")
    except Exception as e:
        st.error(f"Error loading satellite classifier model: {e}")

    img_sat = load_and_preprocess_for_satellite(tmp_path, target_size=(64, 64))
    sat_pred = sat_model.predict(img_sat)[0][0]

    if sat_pred > 0.5:
        sat_label = "Satellite"
        sat_confidence = sat_pred
    else:
        sat_label = "Non Satellite"
        sat_confidence = 1 - sat_pred

    if sat_label != "Satellite":
        st.error("⚠️ Please upload a valid satellite image!")
    else:
        if st.button("Analyze for Drought"):
            with st.spinner("Processing..."):
                try:
                    drought_model = tf.keras.models.load_model("D:\project\drought_detection_finetuned.keras")
                except Exception as e:
                    st.error(f"Error loading drought detection model: {e}")
                    st.stop()

                img_drought = load_and_preprocess_for_drought(tmp_path, target_size=(65, 65))
                drought_pred = drought_model.predict(img_drought)[0][0]

                if drought_pred < 0.5:
                    drought_label = "Drought Detected"
                    drought_confidence = 1 - drought_pred
                else:
                    drought_label = "No Drought Detected"
                    drought_confidence = drought_pred

                st.success("Analysis Complete!")
                fig, ax = plt.subplots(figsize=(4, 4), dpi=150)
                ax.imshow(image)
                ax.set_title(drought_label, fontsize=12, color='red' if "Drought" in drought_label else 'green', pad=6)
                ax.axis('off')
                plt.tight_layout(pad=0.5)
                fig.savefig("temp_result.png", dpi=150, bbox_inches='tight')
                plt.close()

                result_image = Image.open("temp_result.png")
                st.image(result_image, width=350)

                if "No Drought Detected" in drought_label:
                    st.warning("🌱 Normal operations can continue")
                else:
                    st.info("⚠️ Immediate Precaution intervention recommended")
    os.remove(tmp_path)
