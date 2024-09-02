import speech_recognition as sr
from scipy.io import wavfile
from scipy.signal import correlate
import numpy as np

def verify_voice(user_id):
    # ...

    # Load the enrolled voice audio from file
    enrolled_rate, enrolled_data = wavfile.read(f"{user_id}.wav")
    recorded_rate, recorded_data = wavfile.read("recorded.wav")

    # Calculate the energies of the audio signals
    enrolled_energy = np.sum(enrolled_data ** 2)
    recorded_energy = np.sum(recorded_data ** 2)

    # Compare the audio samples using cross-correlation
    similarity = correlate(enrolled_data, recorded_data, mode="full")
    similarity = np.max(similarity)

    # Normalize the similarity value
    normalized_similarity = similarity / (enrolled_energy * recorded_energy + 1e-9)

    print("Normalized similarity:", normalized_similarity)

    # Set a threshold for verification (adjust as needed)
    threshold = 0.8

    if normalized_similarity >= threshold:
        print("Voice verified successfully!")
        return True
    else:
        print("Voice verification failed.")
        return False

# Example usage
user_id = "user_123"
if verify_voice(user_id):
    print("Access granted!")
else:
    print("Access denied.")