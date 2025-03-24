# 📌 AI-Based Multi-Disease Prediction System  
🩺 **An AI-powered web application for predicting Heart Disease, Diabetes, and Chronic Kidney Disease using Machine Learning.**  

## 🔍 Overview  
This project leverages **machine learning algorithms** to provide early diagnosis of **heart disease, diabetes, and kidney disease** based on patient medical data.  
The trained models are deployed using **Streamlit**, allowing users to enter their medical parameters and receive real-time predictions.  

## 🛠️ Features  
✅ **Multi-Disease Prediction** – Supports Heart Disease, Diabetes, and Chronic Kidney Disease diagnosis.  
✅ **Machine Learning Models** – Uses **Random Forest, Logistic Regression, and XGBoost** for high accuracy.  
✅ **Data Preprocessing** – Includes missing value handling, feature scaling, and class balancing (SMOTE).  
✅ **User-Friendly Web Interface** – Developed using **Streamlit** with a clean UI & real-time predictions.  
✅ **Interactive Visualizations** – Displays model performance and health insights.  

## 📂 Project Structure  
AI-Medical-Diagnosis/
│── 📁 data/                        # Datasets used for training  
│   ├── 📝 heart_disease.csv        # Heart Disease dataset  
│   ├── 📝 diabetes.csv             # Diabetes dataset  
│   ├── 📝 kidney_disease.csv       # Kidney Disease dataset  
│  
│── 📁 models/                      # Trained machine learning models  
│   ├── 🔍 rf_heart_balanced.joblib   # Heart Disease Model  
│   ├── 🔍 logreg_diabetes.joblib     # Diabetes Model  
│   ├── 🔍 kidney_disease_model.joblib # Kidney Disease Model  
│  
│── 📁 notebooks/                   # Jupyter Notebooks for model training  
│   ├── 📜 heart_disease.ipynb       # Heart Disease Model Notebook  
│   ├── 📜 diabetes.ipynb            # Diabetes Model Notebook  
│   ├── 📜 kidney_disease.ipynb      # Kidney Disease Model Notebook  
│  
│── 📁 app/                         # Streamlit web application files  
│   ├── 🚀 HDK.py                   # Main Streamlit app file  
│   ├── 🖼️ PICHDK.png                   # UI assets like background images  
│  
│── 📜 requirements.txt             # List of required Python packages  
│── 📜 README.md                    # Project documentation  



## 📊 Machine Learning Models Used  
| **Disease**        | **Best Model Used**     | **Accuracy** |  
|-------------------|-----------------|------------|  
| **Heart Disease** | Random Forest   | 85%        |  
| **Diabetes**      | Logistic Regression | 79%    |  
| **Kidney Disease** | XGBoost         | 92%        |  



## 📝 Datasets Used  
- **[Heart Disease Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)**  
- **[Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)**  
- **[Chronic Kidney Disease Dataset](https://www.kaggle.com/datasets/mansoordaku/ckdisease)**  

---

## 📌 Future Enhancements  
🔹 Improve accuracy using **deep learning models** (ANNs, CNNs).  
🔹 Add more diseases for **early diagnosis**.  
🔹 Deploy on **Hugging Face, AWS, or Google Cloud** for scalability.  

---

## 📬 Contact  
If you have any questions, feel free to reach out! 😊  

📧 **Email**: [nidhisharnagat30@gmail.com](mailto:nidhisharnagat30@gmail.com)  
