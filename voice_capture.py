import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

# Use default microphone
with sr.Microphone() as source:
    print("🎤 Speak something...")
    audio = r.listen(source)
    print("✅ Recording complete.")

    try:
        # Convert speech to text using Google
        text = r.recognize_google(audio)
        print("🗣 You said:", text)
    except sr.UnknownValueError:
        print("❌ Could not understand your voice.")
    except sr.RequestError as e:
        print("❌ Error from Google service:", e)