# Sine Wave Generator and Pentatonic Scale Player

This Python code generates sine waves and plays the pentatonic scale using the `pyaudio` library.

## Requirements

- Python 3.x
- `pyaudio` library

## Installation

1. Clone or download the code from the repository.
2. Install portaudio, a dependency of pyaudio using the the following command:

`brew install portaudio`

3. Install the required `pyaudio` library using the following command:

`pip install pyaudio`


## Usage

1. Run the Python script `sine_wave_pentatonic_scale.py`.
2. The script will generate sine waves for each note in the pentatonic scale and play them.
3. The duration of each note is set to 1 second.
4. Make sure your computer's audio output is configured correctly to hear the generated sound.

## Example

```python
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
