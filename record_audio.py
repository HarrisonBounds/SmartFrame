import pyaudio

# Parameters
FORMAT = pyaudio.paInt16  # Audio format (16-bit)
CHANNELS = 1              # Number of channels (1 for mono)
RATE = 44100              # Sampling rate (samples per second)
CHUNK = 1024              # Buffer size (number of frames per buffer)
RECORD_SECONDS = 5        # Duration of recording in seconds

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

# Capture audio data
audio_data = b""  # Binary string to store audio data
for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    audio_data += data  # Append audio chunks to the string

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Now `audio_data` contains the raw audio as a binary string
print(f"Audio data length: {len(audio_data)} bytes")