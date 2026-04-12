import sounddevice as sd
import numpy as np

# Settings
duration = 5  # seconds
sample_rate = 44100  # Hz

print("Recording...")
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
sd.wait()  # Wait until recording is finished
print("Playing back...")
sd.play(recording, sample_rate)
sd.wait()  # Wait until playback is finished
print("Done!")