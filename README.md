# 🎓 Student Performance Prediction using ANN

## 📌 About Project

This is a simple machine learning project where I built a model to predict whether a student will pass or fail.

The prediction is based on some basic inputs like:
- Study Hours
- Attendance
- Previous Marks
- Assignments Completed
- Sleep Hours

I also created a simple web app using Streamlit where users can give input and see the prediction instantly.

---

## 🧠 What I Used

- Python
- TensorFlow (for ANN model)
- Scikit-learn (for preprocessing)
- Streamlit (for UI)

---

## 🔄 How This Project Works

### Step 1: Data Collection
I created a dataset with student details like study hours, attendance, marks, etc.

---

### Step 2: Data Preprocessing
I split the data into training and testing parts.  
Then I used StandardScaler to scale the data.

---

### Step 3: Model Building
I built an Artificial Neural Network (ANN) using TensorFlow.

- Input: 5 features
- Hidden layers: used ReLU activation
- Output: Sigmoid (gives result between 0 and 1)

---

### Step 4: Training
I trained the model using:
- Binary Cross Entropy loss
- Adam optimizer

---

### Step 5: Evaluation
After training, I tested the model and got around **90% accuracy**.

---

### Step 6: Saving Model
I saved the model and scaler so that I can reuse them in the app.

---

### Step 7: Web App (Streamlit)
I created a simple UI where:
- User can adjust sliders
- Click predict button
- Get PASS / FAIL result
- See confidence score
- See explanation (why result came)

---

## 📊 How Prediction Works

The model gives a value between 0 and 1.

- If value > 0.5 → PASS  
- If value < 0.5 → FAIL  

Example:
- 0.85 → PASS  
- 0.20 → FAIL  

---

## 🚀 How to Run This Project

Follow these steps to run the project on your system:

### 1. Clone the repository
```bash
git clone https://github.com/PyarasaniUday/student-performance-ann.git
cd student-performance-ann

install required libraries
cd pip install -r requirements.txt

Run the application
cd streamlit run app.py


Open in browser