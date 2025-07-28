import random

# Simulated predictions
face_prediction = random.choice([0, 1])   # Simulated: 0 = Truth, 1 = Lie
voice_prediction = random.choice([0, 1])  # Simulated: 0 = Truth, 1 = Lie

print("🧍 Facial model says:", "Lie" if face_prediction else "Truth")
print("🎤 Voice model says:", "Lie" if voice_prediction else "Truth")

# Fusion logic
if face_prediction == 1 and voice_prediction == 1:
    final = "High chance of LIE ❗"
elif face_prediction == 1 or voice_prediction == 1:
    final = "Possible LIE (Uncertain) ⚠️"
else:
    final = "Likely TRUTH ✅"

print("🧠 Final Verdict:", final)