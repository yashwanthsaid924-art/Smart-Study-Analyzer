import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Page config
st.set_page_config(page_title="Smart Study Analyzer", page_icon="🎯", layout="centered")

# Custom CSS (NEW CLEAN DESIGN)
st.markdown("""
<style>
/* Background */
body {
    background-color: #0f172a;
}

/* Main container */
.main {
    background-color: #0f172a;
    color: white;
}

/* Card style */
.block-container {
    padding: 2rem;
    border-radius: 15px;
    background-color: #1e293b;
}

/* Button design */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #3b82f6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 55px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #3b82f6, #6366f1);
    transform: scale(1.03);
}

/* Slider labels */
label {
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Load dataset
data = pd.read_csv("student_data.csv")

# Encode
data['Distraction'] = data['Distraction'].map({'Low': 0, 'Medium': 1, 'High': 2})
data['Productivity'] = data['Productivity'].map({'Low': 0, 'Medium': 1, 'High': 2})

X = data[['Sleep', 'StudyHours', 'Stress', 'Distraction']]
y = data['Productivity']

model = DecisionTreeClassifier()
model.fit(X, y)

# Header
st.markdown("<h1 style='text-align:center;'>🎯 Smart Study Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:lightgray;'>Analyze your habits and improve your productivity 🚀</p>", unsafe_allow_html=True)

st.markdown("---")

# Inputs in columns
col1, col2 = st.columns(2)

with col1:
    sleep = st.slider("😴 Sleep Hours", 0, 10, 6)
    study = st.slider("📚 Study Hours", 0, 10, 4)

with col2:
    stress = st.slider("😓 Stress Level", 1, 10, 5)
    distraction = st.selectbox("📱 Distraction Level", ["Low", "Medium", "High"])

st.markdown("---")

# Convert input
dis_map = {"Low": 0, "Medium": 1, "High": 2}

# Button
if st.button("✨ Analyze My Productivity"):
    
    input_data = pd.DataFrame([[sleep, study, stress, dis_map[distraction]]],
                              columns=['Sleep', 'StudyHours', 'Stress', 'Distraction'])
    
    pred = model.predict(input_data)

    st.markdown("### 📊 Result")

    if pred[0] == 0:
        st.error("😴 Low Productivity")
        st.write("Take rest, reduce stress, and avoid distractions.")
    elif pred[0] == 1:
        st.warning("📚 Medium Productivity")
        st.write("You are doing okay. Try to improve focus.")
    else:
        st.success("🚀 High Productivity")
        st.write("Great job! Keep going with the same routine.")