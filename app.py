import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model # type: ignore

# Load model
model = load_model("model.h5")
scaler = joblib.load("scaler.pkl")

# Page config
st.set_page_config(page_title="Student Performance", layout="centered")

# Title
st.title("🎓 Student Performance Prediction")
st.write("Adjust the sliders to predict student performance")

st.divider()


# INPUT SECTION (SINGLE COLUMN)
st.subheader("📊 Enter Student Details")

hours = st.slider("Study Hours", 0, 12)
attendance = st.slider("Attendance (%)", 0, 100)
marks = st.slider("Previous Marks", 0, 100)
assignments = st.slider("Assignments Completed", 0, 10)
sleep = st.slider("Sleep Hours", 0, 10)

st.divider()


# PREDICT BUTTON
if st.button("🚀 Predict Performance", use_container_width=True):

    data = np.array([[hours, attendance, marks, assignments, sleep]])
    data = scaler.transform(data)

    prediction = model.predict(data)[0][0]

    st.subheader("📊 Result")

   
    # RESULT + EXPLANATION
    if prediction > 0.5:
        st.success("✅ Student will PASS")

        # Explanation (PASS)
        reasons = []
        if marks > 70:
            reasons.append("high marks")
        if attendance > 75:
            reasons.append("good attendance")
        if hours > 5:
            reasons.append("sufficient study hours")
        if assignments > 3:
            reasons.append("completed assignments")

        if reasons:
            st.info("📌 Reason: " + ", ".join(reasons) + " contributed to success.")
        else:
            st.info("📌 Reason: overall balanced performance.")

    else:
        st.error("❌ Student will FAIL")

        # Explanation (FAIL)
        reasons = []
        if marks < 50:
            reasons.append("low marks")
        if attendance < 60:
            reasons.append("poor attendance")
        if hours < 3:
            reasons.append("insufficient study hours")
        if assignments < 2:
            reasons.append("few assignments completed")

        if reasons:
            st.info("📌 Reason: " + ", ".join(reasons) + " affected performance.")
        else:
            st.info("📌 Reason: overall low performance indicators.")

    
    # CONFIDENCE
    st.progress(float(prediction))
    st.write(f"Confidence Score: {prediction:.2f}")