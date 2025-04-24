import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import Flask, request, jsonify


# Load model once when the app starts
model = tf.keras.models.load_model('model/lemon_leafs_model.keras')


# Class labels should match your training classes
class_names = [
    'Anthracnose', 'Bacterial Blight', 'Citrus Canker', 'Curl Virus', 'Deficiency Leaf',
    'Dry Leaf', 'Healthy Leaf', 'Sooty Mould', 'Spider Mites'
]

def predict_image(file):
    img_path = os.path.join('temp', file.filename)
    os.makedirs('temp', exist_ok=True)
    file.save(img_path)

    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)
    predicted_class = class_labels[np.argmax(pred)]
    confidence = round(np.max(pred) * 100, 2)

    os.remove(img_path)
    return predicted_class, confidence
