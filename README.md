Digit-Recognizer

Handwritten digit recognition web app built with Streamlit and a Keras/TensorFlow CNN trained on MNIST.
Users draw digits on a canvas and the app predicts the digit (0–9) in real time.

Project Contents (actual)
Digit-Reco/
├─ .git/
├─ README.md                 # (this file — replace with content below)
├─ app.py                    # Streamlit app (UI + model loading + inference)
├─ digit-reco-colab.ipynb    # Colab notebook: model training & experiments
├─ mnist_cnn_model.h5        # Trained Keras model (used by app.py)
├─ requirements.txt
└─ static/
   └─ digit-image.webp       # static assets used in the app UI


Key facts found in the repository:
App is implemented in app.py and uses Streamlit + streamlit-drawable-canvas.
Model file used: mnist_cnn_model.h5 (loaded via keras.models.load_model(...)).
Notebook for training is present: digit-reco-colab.ipynb.
requirements.txt includes streamlit, tensorflow, numpy, Pillow, and streamlit-drawable-canvas.

Features
Draw a digit (0–9) on a canvas inside the browser.
Preprocessing of the drawing (grayscale, resize, invert/normalize) to match MNIST input.
Predicts digit using the loaded CNN model (mnist_cnn_model.h5).
Clean Streamlit UI with helpful visuals and instant feedback.

Prerequisites
Python 3.8+ recommended (TensorFlow 2.10+ may require specific Python versions).
virtualenv or venv is recommended.

requirements.txt (project contains):
streamlit>=1.20
tensorflow>=2.10
numpy
Pillow
streamlit-drawable-canvas

Quick Start — Run Locally
Clone the repo
git clone https://github.com/your-username/Digit-Reco.git
cd Digit-Reco
(Recommended) Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate


Install dependencies
pip install -r requirements.txt
Run the Streamlit app
streamlit run app.py
Open the app in your browser — Streamlit will print a local URL (usually http://localhost:8501).

How to Use the App
Use the drawing canvas to write a digit with your mouse (or finger on touch devices).
Adjust brush size / background if the UI offers those controls in the sidebar.
Click the predict button (or the app may auto-predict) to see the predicted digit and confidence scores.
Use the “Clear” button to draw a new digit.

Model Details (what’s inside)
Model saved as mnist_cnn_model.h5 — loaded with tensorflow.keras.models.load_model.
Input preprocessing (implemented in app.py) includes:
Converting canvas image to grayscale
Resizing the image to MNIST input size (28×28)
Scaling/normalization to match training preprocessing
Reshaping to model input (1, 28, 28, 1) or similar
The app uses model.predict(...) to get class probabilities and chooses the argmax for the predicted digit.
(For exact architecture and training logs open digit-reco-colab.ipynb.)
Retrain / Improve Model
The repository includes digit-reco-colab.ipynb, a Google Colab notebook with code for training the CNN on MNIST (and possibly improving it). Use that notebook to:

Change architecture (more/less layers)
Modify hyperparameters (epochs, optimizer, learning rate)
Save a new *.h5 model and replace mnist_cnn_model.h5 used by the app

Tip: When saving a new model, keep the same input shape and preprocessing conventions the app expects.

