import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense # type: ignore
import joblib


# 1. Load Dataset
data = pd.read_csv("student_data.csv")
# 2. Features & Target
X = data[['hours_study', 'attendance', 'prev_marks', 'assignments', 'sleep_hours']]
y = data['result']
# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Feature Scaling 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

 
# 5. Build ANN Model
model = Sequential()

model.add(Dense(16, activation='relu', input_dim=5))
model.add(Dense(12, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# 6. Compile Model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)
 
# 7. Train Model
history = model.fit(
    X_train,
    y_train,
    epochs=80,           
    batch_size=8,
    validation_data=(X_test, y_test)
)

# 8. Evaluate Model 
loss, accuracy = model.evaluate(X_test, y_test)
print("\n✅ Model Evaluation:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Loss: {loss:.4f}")

# 9. Save Model & Scaler 
model.save("model.h5")
joblib.dump(scaler, "scaler.pkl")

print("\n✅ Model and Scaler Saved Successfully!")