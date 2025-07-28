import librosa
import numpy as np

# Load audio file
file_path = "sample_audio.wav"
y, sr = librosa.load(file_path)

# Extract MFCCs (Mel-Frequency Cepstral Coefficients)
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
mfcc_mean = np.mean(mfcc.T, axis=0)

print("🎧 MFCC feature shape:", mfcc.shape)
print("🔢 MFCC average values (features):")
print(mfcc_mean)