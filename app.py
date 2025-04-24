import sys
from src.Database import Database 
from flask import Flask
from src import get_config
from blueprints import home, api
from predict import predict_image
from flask import Flask, request, jsonify
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
from werkzeug.utils import secure_filename
model = tf.keras.models.load_model('model/lemon_leafs_model.keras')


# Initialize Flask app with static folder setup
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = get_config("secret_key")

class_labels = [
    'Anthracnose', 'Bacterial Blight', 'Citrus Canker', 'Curl Virus', 'Deficiency Leaf',
    'Dry Leaf', 'Healthy Leaf', 'Sooty Mould', 'Spider Mites'
]


@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('image')
    if not file:
        return jsonify({'error': 'No image uploaded'}), 400

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

    return jsonify({'prediction': predicted_class, 'confidence': float(confidence)})



# Get database connection
db = Database.get_connection()

if db is not None:  # ✅ Explicitly check for None
    print("✅ MongoDB Connection Established!")
    print("Databases:", db.client.list_database_names())  # Check available databases
    print("Collections in 'user':", db.list_collection_names())  # Check collections
else:
    print("❌ Failed to connect to MongoDB.")

# Register Blueprints
app.register_blueprint(home.bp)
app.register_blueprint(api.bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
