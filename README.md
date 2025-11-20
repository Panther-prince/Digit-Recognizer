# Digit-Recognizer
Digit Recognition web application built with Flask and a CNN model (MNIST). Includes canvas drawing, preprocessing, and real-time prediction API

# 🧠 Digit Recognition Web App (MNIST)

This is a deep learning web application that recognizes handwritten digits (0–9) using a CNN trained on the MNIST dataset.

## 🚀 Features
- Draw a digit on canvas
- Real-time prediction using Flask API
- MNIST CNN model (.h5)
- Clean UI with HTML + CSS + JavaScript

## 🗂 Project Structure
DIGIT-RECO/
│── static/
│ └── digit-image.webp
│── templates/
│ └── index.html
│── app.py
│── mnist_cnn_model.h5
│── requirements.txt
│── Procfile

Copy code
🔧 How to Run Locally
bash
Copy code
pip install -r requirements.txt
python app.py
Then open:

cpp
Copy code
http://127.0.0.1:5000/
🌐 Live Demo (Render)
(Will be added after deployment)

📦 Requirements
Python 3.x

Flask

TensorFlow / Keras

NumPy

Pillow

Gunicorn (for deployment)
