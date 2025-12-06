import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from streamlit_drawable_canvas import st_canvas
import base64

# ========================
# PAGE CONFIGURATION
# ========================
st.set_page_config(
    page_title="Digit Recognition AI",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========================
# LOAD BACKGROUND IMAGE
# ========================
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

bg_image = get_base64("static/digit-image.webp")

# ========================
# FULL PAGE CSS - NO SCROLL
# ========================
st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', sans-serif;
        }}

        /* FULL PAGE - NO SCROLL */
        html, body, [data-testid="stAppViewContainer"], .main {{
            height: 100vh;
            overflow: hidden;
        }}

        /* BACKGROUND WITH IMAGE */
        [data-testid="stAppViewContainer"] {{
            {'background-image: url("data:image/webp;base64,' + bg_image + '");' if bg_image else 'background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);'}
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
        }}

        /* DARK OVERLAY */
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.65);
            z-index: 0;
        }}

        /* MAIN CONTENT ABOVE OVERLAY */
        [data-testid="stAppViewContainer"] > div {{
            position: relative;
            z-index: 1;
            height: 100vh;
        }}

        .main .block-container {{
            padding: 1.5rem 2rem;
            max-width: 100%;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        /* HEADER - COMPACT */
        .header-section {{
            text-align: center;
            margin-bottom: 1.5rem;
            padding: 1.5rem 2rem;
            background: rgba(30, 41, 59, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(59, 130, 246, 0.4);
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        }}

        .header-title {{
            font-size: 2.5rem;
            font-weight: 900;
            background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 50%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.25rem;
            letter-spacing: -1px;
        }}

        .header-subtitle {{
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.75);
            font-weight: 500;
        }}

        /* MAIN CONTENT CONTAINER */
        .content-wrapper {{
            flex: 1;
            display: flex;
            gap: 1.5rem;
            min-height: 0;
        }}

        /* COLUMN CARDS */
        .column-card {{
            flex: 1;
            background: rgba(30, 41, 59, 0.9);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(59, 130, 246, 0.5);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}

        /* SECTION HEADERS */
        .section-header {{
            font-size: 1.25rem;
            font-weight: 700;
            color: rgba(255, 255, 255, 0.95);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(59, 130, 246, 0.3);
        }}

        /* CANVAS WRAPPER */
        .canvas-box {{
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
            border: 2px solid rgba(59, 130, 246, 0.5);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            backdrop-filter: blur(10px);
            margin-bottom: 1rem;
        }}

        .canvas-label {{
            font-size: 0.75rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* FIX CANVAS BLACK BACKGROUND */
        [data-testid="stCanvas"] {{
            background: transparent !important;
        }}
        
        [data-testid="stCanvas"] > div {{
            background: transparent !important;
            display: flex !important;
            justify-content: center !important;
        }}

        .canvas-box canvas {{
            border: 2px solid rgba(59, 130, 246, 0.3);
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }}

        /* PREVIEW BOX - COMPACT */
        .preview-box {{
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.95) 100%);
            border: 2px solid rgba(59, 130, 246, 0.5);
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            backdrop-filter: blur(10px);
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        .preview-image {{
            width: 180px;
            height: 180px;
            background: #ffffff;
            border: 2px solid rgba(59, 130, 246, 0.3);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            margin-top: 0.5rem;
        }}

        .preview-image img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            image-rendering: pixelated;
        }}

        .preview-placeholder {{
            color: rgba(0, 0, 0, 0.3);
            font-size: 0.75rem;
            font-weight: 600;
        }}

        /* PREDICTION BOX */
        .prediction-box {{
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(147, 51, 234, 0.15) 100%);
            border: 2px solid rgba(59, 130, 246, 0.6);
            border-radius: 12px;
            padding: 2rem 1.5rem;
            text-align: center;
            backdrop-filter: blur(10px);
            flex: 1;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}

        .prediction-number {{
            font-size: 5rem;
            font-weight: 900;
            background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 50%, #a855f7 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            line-height: 1;
            margin: 0;
            animation: slideIn 0.5s ease;
        }}

        .waiting-text {{
            color: rgba(255, 255, 255, 0.5);
            font-size: 1rem;
            font-weight: 600;
            animation: pulse 2s infinite;
        }}

        .confidence-info {{
            margin-top: 1rem;
            width: 100%;
            max-width: 220px;
        }}

        .confidence-label {{
            font-size: 0.8rem;
            color: rgba(255, 255, 255, 0.9);
            font-weight: 600;
            margin-bottom: 0.5rem;
        }}

        .confidence-bar {{
            width: 100%;
            height: 8px;
            background: rgba(59, 130, 246, 0.2);
            border-radius: 4px;
            overflow: hidden;
        }}

        .confidence-fill {{
            height: 100%;
            background: linear-gradient(90deg, #3b82f6 0%, #60a5fa 100%);
            border-radius: 4px;
            transition: width 0.6s ease;
            box-shadow: 0 0 10px rgba(59, 130, 246, 0.6);
        }}

        /* BUTTONS - COMPACT */
        .stButton > button {{
            width: 100%;
            padding: 0.65rem 1rem !important;
            font-weight: 700 !important;
            font-size: 0.9rem !important;
            border-radius: 10px !important;
            border: none !important;
            transition: all 0.3s ease !important;
            background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
            color: white !important;
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4) !important;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .stButton > button:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.6) !important;
        }}

        /* ANIMATIONS */
        @keyframes slideIn {{
            from {{
                opacity: 0;
                transform: scale(0.8);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}

        @keyframes pulse {{
            0%, 100% {{ opacity: 0.4; }}
            50% {{ opacity: 0.7; }}
        }}

        /* HIDE STREAMLIT BRANDING */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* SIDEBAR STYLING */
        [data-testid="stSidebar"] {{
            background: rgba(15, 23, 42, 0.95) !important;
            border-right: 1px solid rgba(59, 130, 246, 0.3) !important;
        }}

        [data-testid="stSidebar"] > div {{
            background: transparent !important;
        }}

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {{
            color: rgba(255, 255, 255, 0.95) !important;
            font-weight: 700 !important;
        }}

        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label {{
            color: rgba(255, 255, 255, 0.85) !important;
        }}

        /* SIDEBAR CONTROLS */
        .stSelectbox > label,
        .stCheckbox > label,
        .stSlider > label {{
            color: rgba(255, 255, 255, 0.9) !important;
            font-weight: 600 !important;
        }}
        
        /* HIDE SCROLLBAR */
        ::-webkit-scrollbar {{
            display: none;
        }}

        /* RESPONSIVE */
        @media (max-width: 1200px) {{
            .content-wrapper {{ flex-direction: column; }}
            .column-card {{ max-height: 48vh; }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ========================
# LOAD MODEL
# ========================
@st.cache_resource
def load_mnist_model():
    try:
        return load_model("mnist_cnn_model.h5")
    except:
        st.error("❌ Model file 'mnist_cnn_model.h5' not found.")
        st.stop()

model = load_mnist_model()

# ========================
# SESSION STATE
# ========================
if "canvas_key" not in st.session_state:
    st.session_state.canvas_key = 0

# ========================
# SIDEBAR CONTROLS
# ========================
with st.sidebar:
    st.title("⚙️ Controls")
    st.markdown("**Settings & Options**")
    st.markdown("---")
    
    # Input mode
    input_mode = st.selectbox(
        "Input Source",
        options=["Draw (Canvas)", "Upload Image", "Both"],
        index=0
    )
    
    # Stroke width
    stroke_width = st.slider("Brush Size", 4, 40, 18, step=2)
    
    # Canvas size
    canvas_size = st.selectbox("Canvas Size", options=[200, 280, 340, 400, 500], index=4)
    
    st.markdown("---")
    st.markdown("**About**")
    st.info("Draw a digit or upload an image. The model preprocesses images to 28×28 grayscale and predicts in real-time.")
    
    st.markdown("---")
    st.markdown("💡 **Tip:** Draw digits large and clear for best results!")

# ========================
# HEADER
# ========================
st.markdown("""
<div class="header-section">
    <div class="header-title">🔢 Digit Recognition AI</div>
    <div class="header-subtitle">Draw a digit and see AI recognize it instantly • Always live prediction</div>
</div>
""", unsafe_allow_html=True)

# ========================
# MAIN CONTENT - TWO COLUMNS
# ========================
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="medium")

canvas_data = None

# ========================
# LEFT COLUMN - INPUT
# ========================
with col1:
    st.markdown('<div class="column-card">', unsafe_allow_html=True)
    
    # Check input mode
    if input_mode in ("Draw (Canvas)", "Both"):
        st.markdown('<div class="section-header">✏️ Draw Your Digit</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="canvas-box">', unsafe_allow_html=True)
        st.markdown('<div class="canvas-label">Canvas</div>', unsafe_allow_html=True)
        
        canvas_data = st_canvas(
            fill_color="#ffffff",
            stroke_color="#000000",
            stroke_width=stroke_width,
            background_color="#ffffff",
            width=canvas_size,
            height=canvas_size,
            drawing_mode="freedraw",
            key=f"canvas_{st.session_state.canvas_key}",
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Clear button
        if st.button("🗑️ Clear Canvas"):
            st.session_state.canvas_key += 1
            st.rerun()
    
    # Upload option
    uploaded_file = None
    if input_mode in ("Upload Image", "Both"):
        if input_mode == "Both":
            st.markdown('<div style="text-align: center; margin: 1rem 0; color: rgba(255,255,255,0.5); font-weight: 600;">OR</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">📤 Upload Image</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Choose a digit image",
            type=["png", "jpg", "jpeg"],
            help="Upload a clear image of a handwritten digit"
        )
        
        if uploaded_file:
            img_preview = Image.open(uploaded_file)
            st.image(img_preview, caption="Uploaded Image", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ========================
# RIGHT COLUMN - PREDICTION
# ========================
with col2:
    st.markdown('<div class="column-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🎯 Live Prediction</div>', unsafe_allow_html=True)
    
    # Preprocessing function
    def preprocess_pil_image(pil_img):
        img = pil_img.convert("L")
        img = img.resize((28, 28), Image.Resampling.LANCZOS)
        arr = np.array(img)
        arr = 255 - arr
        arr = arr.astype("float32") / 255.0
        arr = arr.reshape(1, 28, 28, 1)
        return arr
    
    def predict_from_array(arr):
        preds = model.predict(arr, verbose=0)
        return int(np.argmax(preds)), preds.squeeze()
    
    # ALWAYS LIVE PREDICTION
    pred_value = None
    pred_probs = None
    
    # Handle uploaded file
    if uploaded_file is not None:
        try:
            uploaded_pil = Image.open(uploaded_file)
            arr = preprocess_pil_image(uploaded_pil)
            pred_value, pred_probs = predict_from_array(arr)
        except Exception as e:
            st.error(f"❌ Upload Error: {e}")
    
    # Handle canvas drawing
    elif canvas_data is not None and canvas_data.image_data is not None:
        try:
            img_array = canvas_data.image_data
            if np.sum(img_array[:, :, :3] < 250) > 100:
                pil_img = Image.fromarray(img_array.astype("uint8")).convert("RGB")
                arr = preprocess_pil_image(pil_img)
                pred_value, pred_probs = predict_from_array(arr)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    
    # Prediction display
    st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
    
    if pred_value is None:
        st.markdown('<div class="waiting-text">Draw to see prediction...</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="prediction-number">{pred_value}</div>', unsafe_allow_html=True)
        
        if pred_probs is not None:
            confidence = float(np.max(pred_probs))
            st.markdown(f'''
            <div class="confidence-info">
                <div class="confidence-label">Confidence: {confidence:.1%}</div>
                <div class="confidence-bar">
                    <div class="confidence-fill" style="width: {confidence*100}%"></div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Preview Section - Moved to right column
    st.markdown('<div class="section-header" style="margin-top: 1rem;">📸 Model Input</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="preview-box">', unsafe_allow_html=True)
    st.markdown('<div class="canvas-label">28x28 Preview</div>', unsafe_allow_html=True)
    
    # Preview logic for both canvas and upload
    preview_image = None
    
    if uploaded_file is not None:
        try:
            uploaded_pil = Image.open(uploaded_file)
            gray_img = uploaded_pil.convert("L")
            resized_img = gray_img.resize((28, 28), Image.Resampling.LANCZOS)
            inverted_img = Image.eval(resized_img, lambda x: 255 - x)
            preview_image = inverted_img.resize((180, 180), Image.Resampling.NEAREST)
        except:
            pass
    elif canvas_data is not None and canvas_data.image_data is not None:
        try:
            img_array = canvas_data.image_data
            if np.sum(img_array[:, :, :3] < 250) > 100:
                pil_img = Image.fromarray(img_array.astype("uint8")).convert("RGB")
                gray_img = pil_img.convert("L")
                resized_img = gray_img.resize((28, 28), Image.Resampling.LANCZOS)
                inverted_img = Image.eval(resized_img, lambda x: 255 - x)
                preview_image = inverted_img.resize((180, 180), Image.Resampling.NEAREST)
        except:
            pass
    
    if preview_image:
        st.image(preview_image, use_container_width=False, width=180)
    else:
        st.markdown('<div class="preview-image"><div class="preview-placeholder">Draw or upload to preview</div></div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)