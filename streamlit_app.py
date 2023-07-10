

import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
import pickle
from PIL import Image


st.set_option('deprecation.showfileUploaderEncoding', False)

@st.cache(allow_output_mutation=True)
def load_model():
	best_model = tf.keras.models.load_model("my_model3.h5")
	return best_model


def predict_class(image, model):
    resized_image = cv2.resize(image, (224,224))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    normalized_image = gray_image / 255.0
    reshaped_image = np.array(normalized_image).reshape(-1, 224, 224, 1)
    y_pred_prob = model.predict(reshaped_image)
    threshold = 0.5
    prediction = (y_pred_prob > threshold).astype(int)
    return prediction


model = load_model()
st.title('Photography Genre Classifier')

file = st.file_uploader("Upload a portrait or a landscape image", type=["jpg", "png"])


if file is None:
	st.text('Waiting for upload....')

else:
	slot = st.empty()
	slot.text('Running inference....')

	test_image = Image.open(file)

	st.image(test_image, caption="Input Image", width = 400)

	pred = predict_class(np.asarray(test_image), model)

	class_names = ['landscape', 'portrait']

	result = class_names[np.argmax(pred)]

	output = 'The photograph is a ' + result

	slot.text('Done')

	st.success(output)

