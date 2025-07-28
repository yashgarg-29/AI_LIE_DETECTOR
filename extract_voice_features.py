import os
import librosa
import numpy as np
import pandas as pd

data = []
labels = []

# Define dataset folders
for label in ['truth', 'lie']:
    folder = f'dataset/{label}'
    for filename in os.listdir(folder):
        if filename.endswith('.wav'):
            filepath = os.path.join(folder, filename)
            y, sr = librosa.load(filepath, sr=None)

            # Extract MFCC features
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            mfcc_mean = np.mean(mfcc.T, axis=0)  # take average of time axis

            data.append(mfcc_mean)
            labels.append(0 if label == 'truth' else 1)

# Convert to DataFrame
df = pd.DataFrame(data)
df['label'] = labels

# Save to CSV
df.to_csv('voice_features.csv', index=False)
print("✅ Saved features to voice_features.csv")