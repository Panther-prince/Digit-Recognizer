# 🧠 Digit Recognizer (0–9) — Streamlit Web App

A simple and interactive **Handwritten Digit Recognition Web Application** built using **TensorFlow/Keras** and **Streamlit**.  
Users can draw digits (0–9) on a canvas, and the trained CNN model predicts the digit in real time.

🚀 **Live Demo:**  
🔗 https://digit-recognizer-0-9.streamlit.app/

📦 **GitHub Repository:**  
🔗 https://github.com/Panther-prince/Digit-Recognizer

---

## 📁 Project Structure

Digit-Recognizer/
│── app.py # Main Streamlit application
│── digit-reco-colab.ipynb # CNN model training notebook (Google Colab)
│── mnist_cnn_model.h5 # Trained MNIST CNN model
│── requirements.txt # Dependencies
│── README.md # Documentation
│── static/
│ └── digit-image.webp # App UI image

yaml
Copy code

---

## ✨ Features

- ✍️ Draw digits directly inside the browser (0–9)
- 🎛️ Canvas built using **streamlit-drawable-canvas**
- 🧼 Automatic image preprocessing (grayscale → resize → normalize)
- 🔮 Real-time digit prediction using **CNN model**
- 📊 Probability scores for each digit
- 🧱 Clean & minimal Streamlit interface
- 📚 Colab notebook included for retraining and experimentation

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **TensorFlow / Keras**
- **Streamlit**
- **NumPy**
- **Pillow**
- **streamlit-drawable-canvas**

---

## 📦 Installation Guide

Follow the steps below to run the project locally:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Panther-prince/Digit-Recognizer.git
cd Digit-Recognizer
2️⃣ Create a Virtual Environment (Recommended)
Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
macOS / Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Streamlit App
bash
Copy code
streamlit run app.py
➡️ Open your browser and go to:
http://localhost:8501

🧠 Model Details
Model used: mnist_cnn_model.h5
Trained on MNIST dataset (70,000 handwritten digits)
Based on a CNN architecture (Conv2D, MaxPooling, Dense layers)
Input Preprocessing Steps:
Convert drawing → grayscale
Resize to 28 × 28
Normalize pixel values (0–1)
Reshape to (1, 28, 28, 1)
Predict using:
python
Copy code
model.predict(img)
🔄 Retraining the Model
Use the Google Colab notebook:
📄 digit-reco-colab.ipynb
You can:
Modify CNN architecture
Tune hyperparameters
Train longer

Export a new .h5 model

Replace the existing mnist_cnn_model.h5 to update the web app.
