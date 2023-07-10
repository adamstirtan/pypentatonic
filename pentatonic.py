import numpy as np
import pyaudio

# Set up the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)

# Define the pentatonic scale frequencies
pentatonic_scale = [261.63, 293.66, 329.63, 392.00, 440.00, 523.25]

# Generate and play the sine waves
for freq in pentatonic_scale:
    duration = 1.0  # Duration in seconds
    t = np.linspace(0, duration, int(duration * 44100), False)
    samples = np.sin(2 * np.pi * freq * t)
    stream.write(samples.astype(np.float32).tobytes())

# Clean up the audio stream and terminate PyAudio
stream.stop_stream()
stream.close()
p.terminate()
