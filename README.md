Digit-Recognizer

A handwritten digit recognition web application built using Streamlit and a Keras/TensorFlow CNN trained on the MNIST dataset.
Users can draw digits (0–9) on a canvas, and the app predicts the digit in real time.

📁 Project Structure
Digit-Reco/
├─ .git/
├─ README.md
├─ app.py                    # Streamlit app (UI + model loading + prediction)
├─ digit-reco-colab.ipynb    # Google Colab notebook for model training
├─ mnist_cnn_model.h5        # Trained MNIST CNN model
├─ requirements.txt
└─ static/
   └─ digit-image.webp        # Static asset used in UI

✔ Key Facts

Built completely in Streamlit using streamlit-drawable-canvas.

Model used: mnist_cnn_model.h5 loaded using keras.models.load_model().

Training notebook available: digit-reco-colab.ipynb.

Dependencies include Streamlit, TensorFlow, NumPy, Pillow, and Canvas integration.

✨ Features

Draw digits (0–9) directly in the browser.

Converts drawing to grayscale, resizes to 28×28, and normalizes like MNIST.

CNN model predicts the digit with confidence scores.

Clean and modern Streamlit interface.

Instant prediction output.

🛠 Prerequisites

Python 3.8+

Recommended: create a virtual environment

requirements.txt includes:
streamlit>=1.20
tensorflow>=2.10
numpy
Pillow
streamlit-drawable-canvas

🚀 Run the Project Locally
1. Clone the repository
git clone https://github.com/your-username/Digit-Reco.git
cd Digit-Reco

2. Create & activate a virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

macOS / Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit app
streamlit run app.py


Then open your browser at:

👉 http://localhost:8501

🧑‍💻 How to Use the App

Draw a digit using your mouse or touch device.

Adjust brush size if needed from the sidebar.

Click Predict (or automatic prediction will trigger).

The predicted digit and confidence scores will appear.

Press Clear to try again.

🧠 Model Details

Model file: mnist_cnn_model.h5

Loaded via:

tensorflow.keras.models.load_model("mnist_cnn_model.h5")


Preprocessing steps used in app.py:

Convert drawing to grayscale

Resize to 28×28

Normalize pixel values

Reshape to (1, 28, 28, 1) for CNN input

Prediction is performed via:

model.predict(...)


The highest probability (argmax) gives the predicted digit.

(See the digit-reco-colab.ipynb notebook for architecture details and training logs.)

🔁 Retrain / Improve the Model

The included Colab notebook lets you:

Modify CNN architecture

Change hyperparameters (optimizer, LR, epochs …)

Retrain and export a new .h5 model

Replace mnist_cnn_model.h5 inside the project

Important:
If you retrain, maintain the same input shape and preprocessing expected by the app.
