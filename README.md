# 🧠 Digit Recognition Web App (MNIST)

This is a Flask-based web application that recognizes handwritten digits (0–9).  
The backend uses a trained CNN MNIST model (`mnist_cnn_model.h5`), and the frontend provides a drawing canvas for users to draw digits.

---

## 🚀 Features
- Draw digits on a canvas
- Sends image to Flask API for prediction
- MNIST CNN Model for accurate results
- Clean UI (HTML, CSS, JS)
- Fully deployable on Render (Free)

---

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
│── README.md
│── .gitignore

yaml
Copy code

---

## 🔧 How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Run the Flask app
bash
Copy code
python app.py
3. Open in browser
cpp
Copy code
http://127.0.0.1:5000/
🌐 Deployment (Render)
Push project to GitHub

Go to https://render.com

Create new Web Service

Build command:

nginx
Copy code
pip install -r requirements.txt
Start command:

nginx
Copy code
gunicorn app:app
Select Free Tier

Deploy 🚀

📦 Requirements
Python 3.x

Flask

TensorFlow / Keras

NumPy

Pillow

👨‍💻 Author
Prince Y. Raval

yaml
Copy code

---

# ✅ **4. .gitignore**

Create a file named **.gitignore** and paste this:

Python cache
pycache/
*.pyc

Virtual environments
venv/
env/

VS Code settings
.vscode/
.idea/

OS files
.DS_Store
Thumbs.db

yaml
Copy code

⚠️ NOTE:  
We **do NOT ignore `.h5` model** because Render needs it.
