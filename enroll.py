import speech_recognition as sr

def enroll_voice():
    # Create a speech recognition object
    r = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something to enroll your voice:")
        audio = r.listen(source)

        # Generate a unique ID for the user
        user_id = "user_123"

        # Save the audio to a file for later verification
        with open(f"{user_id}.wav", "wb") as f:
            f.write(audio.get_wav_data())

    print("Voice enrolled successfully!")

enroll_voice()