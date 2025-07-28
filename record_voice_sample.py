import os
import sounddevice as sd
from scipy.io.wavfile import write

label = input("Enter label (truth or lie): ").lower()
filename = input("Enter sample name (e.g. truth1 or lie5): ")

directory = f"dataset/{label}"
os.makedirs(directory, exist_ok=True)

fs = 44100  # Sampling rate
duration = 5  # seconds

print(f"🎤 Speak now for label '{label}'...")
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print("✅ Recording complete.")

filepath = f"{directory}/{filename}.wav"
write(filepath, fs, recording)
print(f"📁 Saved: {filepath}")