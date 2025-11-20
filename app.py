from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import base64
import io

app = Flask(__name__)

# Load your MNIST model
model = load_model("mnist_cnn_model.h5")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data or "image" not in data:
            return jsonify({"error": "No image received"}), 400

        # Base64 → PIL Image
        image_data = data["image"].replace("data:image/png;base64,", "")
        img_bytes = base64.b64decode(image_data)
        img = Image.open(io.BytesIO(img_bytes)).convert("L")  # gray

        # MNIST Preprocessing
        img = img.resize((28, 28))
        img = np.array(img)

        img = 255 - img               # invert (white digit on black)
        img = img.astype("float32") / 255.0
        img = img.reshape(1, 28, 28, 1)

        # Predict
        prediction = model.predict(img)
        digit = int(np.argmax(prediction))

        return jsonify({"digit": digit})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
