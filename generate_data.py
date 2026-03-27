import pandas as pd
import random

data = []

for i in range(200):
    hours = random.randint(0, 10)
    attendance = random.randint(40, 100)
    marks = random.randint(30, 100)
    assignments = random.randint(0, 5)
    sleep = random.randint(4, 9)

    # Strong logical rule (no nonsense)
    score = (
        hours * 2 +
        attendance * 0.4 +
        marks * 0.6 +
        assignments * 5
    )

    # Controlled noise (small only)
    score += random.uniform(-10, 10)

    # Logical decision
    if score > 140:
        result = 1
    elif score < 100:
        result = 0
    else:
        result = 1 if marks > 60 else 0   # fallback logic

    data.append([hours, attendance, marks, assignments, sleep, result])

df = pd.DataFrame(data, columns=[
    "hours_study", "attendance", "prev_marks", "assignments", "sleep_hours", "result"
])

df.to_csv("student_data.csv", index=False)

print("✅ Balanced dataset created")