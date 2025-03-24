import streamlit as st
import numpy as np
import base64
from joblib import load
import requests
from streamlit_lottie import st_lottie  # For animations

# Function to set a background image
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read()).decode()
    
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center center;
        background-attachment: fixed;
        animation: fadeIn 0.5s ease-in-out;
    }}

    /* Glassmorphism for Subtitle Only */
    .glass-subtitle {{
        background: rgba(255, 255, 255, 0.2);  /* Transparent white */
        backdrop-filter: blur(10px);  /* Blurry effect */
        border-radius: 15px;
        padding: 15px 30px;
        display: inline-block;
        text-align: center;
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);
        animation: fadeIn 0.5s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}

    
    </style>
""", unsafe_allow_html=True)
    
    
# Set the background image
set_background("PICHDK.png")

# Function to load Lottie animation from a URL (cached for performance)
@st.cache_resource
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Load models once & store in memory
@st.cache_resource
def load_model(file_path):
    return load(file_path)

# Load models and store them in session state
if "heart_disease_model" not in st.session_state:
    st.session_state.heart_disease_model = load_model("rf_heart_balanced.joblib")

if "diabetes_model" not in st.session_state:
    st.session_state.diabetes_model = load_model("logreg_diabetes.joblib")

if "kidney_disease_model" not in st.session_state:
    st.session_state.kidney_disease_model = load_model("kidney_disease_model.joblib")

# Cache predictions to avoid recomputation
@st.cache_data
def predict_disease(_model, input_data):
    return _model.predict(input_data)[0]

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'selected_disease' not in st.session_state:
    st.session_state.selected_disease = None

# Function to navigate between pages
def change_page(page_name):
    st.session_state.page = page_name

# 🌟 Apply Custom Styling
st.markdown("""
    <style>
    
    /* Title Styling */
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        background: linear-gradient(to right, #B983FF, #7B2CBF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Roboto', sans-serif;
        text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
    }

    /* Subtitle Styling */
    .glass-subtitle-text {
        text-align: center;
        font-size: 28px;
        font-family: 'Roboto', sans-serif;
        font-weight: bold;
        background: linear-gradient(135deg, #A663CC, #7B2CBF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    .glass-subtitle-emoji  {
        font-size: 28px;
        font-weight: bold;
        color: #7B2CBF; /* Solid color for emojis */
    }
    
     /* Adjusting input fields */
    .stTextInput, .stNumberInput, .stSelectbox, .stRadio {
        background-color: #EBD9FF !important;  /* Light Purple */
        border-radius: 8px !important;
        border: 2px solid #A663CC !important;
        color: #5A189A !important;  /* Deep Purple for better contrast */
        font-weight: bold !important;
    }
  
    /* Adjust labels for better readability */
    label, span {
        color: #5A189A !important;  /* Deep Purple Text */
        font-weight: bold !important;
    }
    
  
    /* If the title is the direct child and options are nested in a div */
    div.stRadio > label:first-child {
        color: #5A189A !important;
        font-weight: bold !important;
    }

    div.stRadio > div label {
        color: black !important;
        font-weight: normal !important;
    }

    /* 3D Button Effect */
    .stButton>button {
        background: linear-gradient(135deg, #A663CC, #7B2CBF);
        color: white !important;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #D0AFFF, #B983FF);
        transform: translateY(-3px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #A663CC !important;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
    }
    
    
    /* Enhancing White Text for Visibility */
    h1, h2, h3, h4, h5, h6, p {
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7); /* Stronger contrast */
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="glass-box"><h1 class="title">HDK-AI Medical Diagnosis Pro 🩺</h1></div>', 
    unsafe_allow_html=True
)
st.markdown("""
    <div style="text-align: center;">
        <div class="glass-subtitle">
            <span class="glass-subtitle-text">Your Health, Our Priority – AI-Driven Diagnosis</span> 
            <span class="glass-subtitle-emoji">💡</span>
        </div>
    </div>
""", unsafe_allow_html=True)




# 🌟 **Page 1: Welcome Page**
if st.session_state.page == "home":
    # Disease selection with interactive cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Heart Disease ❤️", key="heart"):
            st.session_state.selected_disease = "Heart Disease"
            change_page("input_page")
    with col2:
        if st.button("Diabetes 🍩", key="diabetes"):
            st.session_state.selected_disease = "Diabetes"
            change_page("input_page")
    with col3:
        if st.button("Kidney Disease 🧑‍⚕️", key="kidney"):
            st.session_state.selected_disease = "Kidney Disease"
            change_page("input_page")

    # Show a Lottie animation for page load or when user selects the disease
    lottie_loading = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_8gndmu0i.json")
    if lottie_loading:
        st_lottie(lottie_loading, speed=1, width=600, height=400, key="loading")








# 🌟 **Page 2: Input Form Page**
elif st.session_state.page == "input_page":
    st.markdown(f"<h2 style='text-align: center;'>Enter Details for {st.session_state.selected_disease}</h2>", unsafe_allow_html=True)

    if st.session_state.selected_disease == "Heart Disease":
        st.markdown("<h4 style='font-weight: bold;'>General Information</h4>", unsafe_allow_html=True)
        age = st.number_input("Age 👶👴", min_value=1, max_value=100, value=30, step=1, help="Enter the age of the patient.\n"
                              "Older individuals are at higher risk for heart diseases.")

        st.markdown("<h4 style='font-weight: bold;'>Heart Function Tests</h4>", unsafe_allow_html=True)
        blood_pressure = st.number_input("Blood Pressure (mm Hg) 📈", min_value=50, max_value=200, value=120, step=1, 
                                         help="Blood pressure measures how forcefully your heart pumps blood.\n "
                                          "A reading above **130/80 mm Hg** indicates hypertension, increasing heart disease risk.")
        cholesterol = st.number_input("Cholesterol Level (mg/dL) 🧴", min_value=100, max_value=500, value=200, step=1, 
                                       help="Cholesterol is a type of fat in your blood.\n"
                                       "A total cholesterol level above **240 mg/dL** is high and increases the risk of heart disease.")
        max_hr = st.number_input("Maximum Heart Rate ❤️", min_value=50, max_value=250, value=150, step=1, 
                                 help="The highest heart rate your body can achieve during exercise.\n "
                                  "Lower values may indicate poor heart health.")
        oldpeak = st.number_input("ST Depression 📉", min_value=0.0, max_value=10.0, value=1.0, step=0.1, 
                                  help="ST depression during exercise is a sign of ischemia (reduced blood flow to the heart).\n "
                                   "Higher values (above **2.0 mm**) may indicate severe heart problems.")

        st.markdown("<h4 style='font-weight: bold;'>Risk Factors</h4>", unsafe_allow_html=True)
        fasting_bs = st.number_input("Fasting Blood Sugar (mg/dL) 🍩", min_value=50, max_value=300, value=100, step=1, 
                                     help="Measures blood sugar levels after fasting for at least 8 hours.\n"
                                     "**Above 120 mg/dL** suggests diabetes, which increases heart disease risk.")
        fasting_bs_flag = 1 if fasting_bs > 120 else 0  # Auto-classify >120 mg/dL as 1
        sex = st.selectbox("Sex 👨👩", ["Male", "Female"],
                                        help="Males generally have a higher risk of heart disease,\n" 
                                        "but after menopause, the risk increases for females as well.")     
        chest_pain = st.selectbox("Chest Pain Type 💔", [
            "Typical Angina (ATA)", "Atypical Angina (TA)", 
            "Non-Anginal Pain (NAP)", "Asymptomatic (ASY)"
        ],
                                   help="Different types of chest pain:\n"
             "- **Typical Angina (ATA)**: Chest pain due to reduced blood flow, occurs during activity.\n"
             "- **Atypical Angina (TA)**: Unusual chest pain, might occur at rest.\n"
             "- **Non-Anginal Pain (NAP)**: Chest discomfort **not related** to heart disease.\n"
             "- **Asymptomatic (ASY)**: No chest pain but still at risk.")
        resting_ecg = st.selectbox("Resting ECG 🧠", [
            "Normal", "ST-T Wave Changes (ST)", "Left Ventricular Hypertrophy (LVH)"
        ], 
                                   help="ECG measures the electrical activity of your heart:\n"
             "- **Normal**: No abnormality detected.\n"
             "- **ST-T Wave Changes (ST)**: May indicate reduced blood flow to the heart.\n"
             "- **Left Ventricular Hypertrophy (LVH)**: Thickening of the heart walls due to high blood pressure.")
        exercise_angina = st.selectbox("Exercise-Induced Angina 🏃", ["No", "Yes"], 
                                       help="Pain or discomfort in the chest **during physical activity**.\n "
                                    "It indicates that your heart is not getting enough oxygen-rich blood.")
        st_slope = st.selectbox("ST Slope ⬆️⬇️", [
            "Up (Healthy)", "Flat (Moderate Risk)", "Down (High Risk)"
        ], help="Indicates how your heart responds to exercise:\n"
             "- **Up (Healthy)**: Normal response, **low risk**.\n"
             "- **Flat (Moderate Risk)**: May suggest blocked arteries.\n"
             "- **Down (High Risk)**: Strong indication of serious heart disease.")

        # Convert categorical inputs into numerical values
        inputs = [
            age, blood_pressure, cholesterol, max_hr, oldpeak, 
            sex == "Male", chest_pain.startswith("Typical Angina"), chest_pain.startswith("Atypical Angina"), 
            chest_pain.startswith("Non-Anginal Pain"), resting_ecg.startswith("Normal"), resting_ecg.startswith("ST"), 
            exercise_angina == "Yes", st_slope.startswith("Flat"), st_slope.startswith("Up"), fasting_bs_flag
        ]
        
        
        
        
        
        
        
        
    elif st.session_state.selected_disease == "Diabetes":
       # Group: General Information
        st.markdown("<h4 style='font-weight: bold;'>General Information</h4>", unsafe_allow_html=True)
        age = st.number_input("Age 👶👴", min_value=1, max_value=100, value=30, step=1, 
                              help="Your age in years.\n The risk of diabetes increases with age, especially after **45 years**.")
        # Group: Health Metrics
        st.markdown("<h4 style='font-weight: bold;'>Health Metrics 📊</h4>", unsafe_allow_html=True)
        pregnancies = st.number_input("Pregnancies 👶", min_value=0, max_value=20, value=0, step=1,  
                                      help="For females, more pregnancies may increase the risk of diabetes. "
                                       "For males, enter **0** as it's not applicable.")
    
        glucose = st.number_input("Glucose Level 🩸", min_value=50, max_value=300, value=100, step=1, 
                                  help="Measures blood sugar levels. **Fasting glucose over 126 mg/dL** "
                                   "or **random glucose over 200 mg/dL** may indicate diabetes.")
        blood_pressure = st.number_input("Blood Pressure 📈", min_value=50, max_value=200, value=120, step=1, 
                                         help="Blood pressure measures the force of blood against artery walls. "
                                          "**Above 130/80 mm Hg** increases the risk of diabetes complications.")
        skin_thickness = st.number_input("Skin Thickness 📏", min_value=0, max_value=50, value=0, step=1, 
                                         help="Measures the thickness of the skin fold in the triceps area. "
                                          "**Higher values** are associated with obesity and insulin resistance.")
        insulin = st.number_input("Insulin Level 🩸", min_value=0, max_value=900, value=0, step=1, 
                                  help="Insulin helps control blood sugar. **Low levels** may indicate Type 1 diabetes, "
                                   "while **high levels** may suggest insulin resistance (Type 2 diabetes).")

        bmi = st.number_input("Body Mass Index (BMI) ⚖️", min_value=10, max_value=50, value=25, step=1, 
                              help="BMI is a measure of body fat based on height and weight. **Above 25** is overweight, "
                               "and **above 30** is obese, increasing the risk of diabetes.")
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function 🧬", min_value=0.0, max_value=2.5, value=0.0, step=0.1, 
                                                     help="A score based on family history of diabetes. **Higher values (>0.8)** indicate a greater genetic risk.")


        # All inputs
        inputs = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]












    elif st.session_state.selected_disease == "Kidney Disease":
        # Group: General Information
        st.markdown("<h4 style='font-weight: bold;'>General Information</h4>", unsafe_allow_html=True)
        age = st.number_input("Age 🧑‍🦱", min_value=1, max_value=100, value=20, step=1, help="Age of the patient.\n"
                              "Young, less risk.\n"
                              "Older individuals are more prone.")
        
        # Group: Blood Pressure
        st.markdown("<h4 style='font-weight: bold;'>Blood Pressure 📊</h4>", unsafe_allow_html=True)
        blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=50, max_value=200, value=100, step=1, help="Blood pressure in mm Hg.\n"
                                         "**[Normal: 120/80]**")

        # Group: Urine & Blood Test Results
        st.markdown("<h4 style='font-weight: bold;'>Urine & Blood Test Results</h4>", unsafe_allow_html=True)
        specific_gravity = st.number_input("Specific Gravity 🧴", min_value=1.000, max_value=1.050, value=1.020, step=0.001, 
                                           help="Specific Gravity measures kidney's ability to concentrate urine.\n"
                                           "Lower values indicate kidney issues.\n"
                                           "**[Normal Range: 1.015 - 1.025].**")
        albumin = st.number_input("Albumin (mg/dL) 💉", min_value=0.0, max_value=5.0, value=2.0, step=0.1, 
                                  help="Albumin level in the blood.\n"
                                  "Higher values suggest kidney damage.")
        sugar_level = st.number_input("Sugar Level 🩸", min_value=0.0, max_value=1000.0, value=150.0, step=1.0, 
                                      help="Blood sugar level.\n"
                                      "Presence of sugar in Urine can indicate problems.")
        red_blood_cells = st.selectbox("Red Blood Cells (RBCs) 🩸", ["Normal", "Abnormal"], help="Presence of red blood cells in urine.")
        pus_cell = st.selectbox("Pus Cells ⚠️", ["Normal", "Abnormal"], help="Presence of pus cells in urine.")
        
        # **Adding Blood Glucose Random**
        blood_glucose_random = st.number_input("Blood Glucose Random 🩸", min_value=0.0, max_value=1000.0, value=150.0, step=1.0, help="Random blood glucose level measurement.\n **[Healthy: 80-120]**")
        
        # Group: Kidney Function Tests
        st.markdown("<h4 style='font-weight: bold;'>Kidney Function Tests</h4>", unsafe_allow_html=True)
        blood_urea = st.number_input("Blood Urea (mg/dL) 💉", min_value=0.0, max_value=100.0, value=20.0, step=0.1, help="Blood urea nitrogen levels. \n **[Healthy: < 20]**")
        serum_creatinine = st.number_input("Serum Creatinine (mg/dL) 🧪", min_value=0.0, max_value=10.0, value=1.0, step=0.1, help="Serum creatinine level. \n **[Healthy: 0.6 - 1.2]**")
        sodium = st.number_input("Sodium (mEq/L) 🔋", min_value=100.0, max_value=150.0, value=135.0, step=1.0, help="Sodium level in the blood. \nLower sodium indicates kidney dysfunction.\n **[Healthy: 135-145]**")
        potassium = st.number_input("Potassium (mEq/L) ⚡", min_value=3.0, max_value=7.0, value=4.5, step=0.1, help="Potassium level in the blood. \n Elevated potassium is a red flag.\n **[Healthy: 3.5-5.0]**")
        
        # Group: Symptoms & Conditions
        st.markdown("<h4 style='font-weight: bold;'>Symptoms & Conditions</h4>", unsafe_allow_html=True)
        hemoglobin = st.number_input("Hemoglobin Level 🩸", min_value=0.0, max_value=20.0, value=13.5, step=0.1, help="Hemoglobin level in g/dL.\n **[Normal Range: 12-17].**")
        packed_cell_volume = st.number_input("Packed Cell Volume 📊", min_value=20.0, max_value=50.0, value=45.0, step=0.1, help="Packed cell volume in percentage.\n Low PCV is a sign of CKD.\n **[Normal: 40-50].**")
        white_blood_cell_count = st.number_input("White Blood Cell Count 🩸", min_value=3000, max_value=12000, value=5000, step=1, help="White blood cell count. \n**[Normal: 4000-11000].**")
        red_blood_cell_count = st.number_input("Red Blood Cell Count 🩸", min_value=3.0, max_value=6.0, value=5.0, step=0.1, help="Red blood cell count.\n **[Healthy: 4.7-6.1].**")
        
        # Group: Health Conditions (Binary)
        st.markdown("<h4 style='font-weight: bold;'>Health Conditions</h4>", unsafe_allow_html=True)
        appetite = st.selectbox("Appetite 🍽️", ["Good", "Poor"], help="How is the patient's appetite?")
        hypertension = st.radio("Hypertension 🩸", ["No", "Yes"], help="Does the patient have hypertension?")
        coronary_artery_disease = st.radio("Coronary Artery Disease 🫀", ["No", "Yes"], help="Does the patient have coronary artery disease?")
        diabetes_mellitus = st.radio("Diabetes Mellitus 🩸", ["No", "Yes"], help="Does the patient have diabetes?")
        pedal_edema = st.radio("Pedal Edema 🦶", ["No", "Yes"], help="Does the patient have swelling in the legs (pedal edema)?")
        anemia = st.radio("Anemia 🩸", ["No", "Yes"], help="Does the patient have anemia?")

        # All inputs
        inputs = [
            age, blood_pressure, specific_gravity, albumin, sugar_level, red_blood_cells == "Abnormal",
            pus_cell == "Abnormal", blood_urea, serum_creatinine, sodium, potassium, hemoglobin, 
            packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension == "Yes", 
            coronary_artery_disease == "Yes", diabetes_mellitus == "Yes", pedal_edema == "Yes", anemia == "Yes", 
            blood_glucose_random, appetite == "Poor"
        ]
        











    # Floating Action Button for Prediction
    if st.button("Predict 💡", key="predict", help="Click to predict disease status"):
        st.session_state.inputs = np.array([inputs])
        change_page("result_page")

# 🌟 **Page 3: Prediction Result Page**
elif st.session_state.page == "result_page":
    st.markdown(f"""
            <div class="glass-box">
                <h2 style='text-align: center;'>Diagnosis Result for {st.session_state.selected_disease}</h2>
            </div>
        """, unsafe_allow_html=True)    
    
    # Lottie Animation for loading prediction
    lottie_animation = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_8gndmu0i.json")
    if lottie_animation:
        st_lottie(lottie_animation, speed=1, width=600, height=400, key="loading")

  # Predict and display result
    model = st.session_state[st.session_state.selected_disease.lower().replace(" ", "_") + "_model"]
    pred = predict_disease(model, st.session_state.inputs)
    result = "Positive⚠️" if pred == 1 else "Negative💝"
    color_positive = "#F44336"  # Red for Positive
    color_negative = "#4CAF50"  # Solid Green for Negative

    color = color_positive if pred == 1 else color_negative

    # Result Box with smoother style
    st.markdown(f"""
    <div style="background: {color}; color: white; padding: 20px; border-radius: 15px; 
                text-align: center; font-size: 24px; font-weight: bold; 
                box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.4); animation: fadeIn 0.5s ease-in-out;">
        🏥 Diagnosis Result: {result}
    </div>
""", unsafe_allow_html=True)

    
    if st.button("Go to Home 🏠"):
        change_page("home")



 