from flask import Blueprint, request, redirect, url_for, session, flash
from src.Auth import Auth
from flask import Blueprint, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os
from werkzeug.utils import secure_filename

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    result = Auth.register(name, email, password)
    if result == "Registration successful":
        return redirect(url_for("home.dashboard"))
    else:
        flash(result)
        return redirect(url_for("home.home"))

@bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        result = Auth.login(email, password)
        if result == "Login successful":
            return redirect(url_for("home.dashboard"))
        else:
            flash(result)
            return redirect(url_for("home.home"))
    return render_template("index.html")  # Your login page template

@bp.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    filename = secure_filename(image.filename)
    filepath = os.path.join('temp_uploads', filename)
    os.makedirs('temp_uploads', exist_ok=True)
    image.save(filepath)

    try:
        img = load_img(filepath, target_size=(150, 150))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))

        return jsonify({
            'predicted_class': predicted_class,
            'confidence': round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if os.path.exists(filepath):
            os.remove(filepath)







