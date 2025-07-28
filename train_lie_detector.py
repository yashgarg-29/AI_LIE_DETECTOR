from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib
# Dummy dataset (each row = MFCC features)
X = np.random.rand(10, 13)  # 10 samples, 13 features each (like MFCC)
y = [0, 1, 1, 0, 0, 1, 1, 0, 0, 1]  # Labels: 0 = Truth, 1 = Lie

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Test on a new sample
test_sample = X[0].reshape(1, -1)  # One sample to predict
prediction = model.predict(test_sample)

print("✅ Prediction (0 = Truth, 1 = Lie):", prediction[0])
joblib.dump(model, "voice_model.pkl")  # Save model to file