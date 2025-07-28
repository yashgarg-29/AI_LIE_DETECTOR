import tkinter as tk
from tkinter import messagebox
import random
import joblib
import librosa
import numpy as np
import speech_recognition as sr
# Function to simulate face + voice prediction
# Load saved voice model
voice_model = joblib.load("voice_model.pkl")

# Real voice + model prediction
def detect_lie():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)
        print("✅ Voice recorded")

    # Save temporary audio file
    with open("temp.wav", "wb") as f:
        f.write(audio.get_wav_data())

    try:
        y, sr_rate = librosa.load("temp.wav")
        mfcc = librosa.feature.mfcc(y=y, sr=sr_rate, n_mfcc=13)
        mfcc_mean = np.mean(mfcc.T, axis=0).reshape(1, -1)

        voice_pred = voice_model.predict(mfcc_mean)[0]
    except:
        messagebox.showerror("Error", "Voice analysis failed.")
        return

    # Simulate face result for now
    from face_predictor import detect_face_lie
    face_pred = detect_face_lie()
    # Fusion logic
    if face_pred == 1 and voice_pred == 1:
        verdict = "High chance of LIE ❗"
        color = "red"
    elif face_pred == 1 or voice_pred == 1:
        verdict = "Possible LIE (Uncertain) ⚠️"
        color = "orange"
    else:
        verdict = "Likely TRUTH ✅"
        color = "green"

    result_label.config(text=verdict, fg=color)
    with open("results_log.txt", "a") as log:
        log.write(f"Face: {face_pred}, Voice: {voice_pred} → {verdict}\n")


# GUI window
app = tk.Tk()
app.title("AI-Based Lie Detector")
app.geometry("400x250")
app.config(bg="#f0f0f0")

tk.Label(app, text="Lie Detector", font=("Helvetica", 20, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Button(app, text="Start Detection", font=("Helvetica", 14), command=detect_lie).pack(pady=20)

result_label = tk.Label(app, text="", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
result_label.pack(pady=20)

app.mainloop()