import sounddevice as sd
from scipy.io.wavfile import write
import keyboard
import numpy as np
import sys
import time

# Now, before starting the recorder, we have to declare a few variables. The first one is the sampling frequency of the
# audio (in most cases this will be 44100 or 48000 frames per second) and the second is recording duration. We have to
# specify the duration in seconds so that it stops recording after that duration.


print("Press r for  to start recording.")
print("Press Enter  to stop recording.")

frequency = 44100


def start_recording():
    print("🚀 Recording started...")
    recordings = []
    while True:
        # Record audio in chunks of 0.1 seconds
        chunk = sd.rec(int(0.1 * frequency), samplerate=frequency, channels=2)
        sd.wait()
        recordings.append(chunk)  # Append the recorded chunk

        # Stop recording if 'Enter' is pressed
        if keyboard.is_pressed('enter'):
            print("🚀 'Recording has been completed'!")
            break
    # Combine all recorded chunks into one array
    full_recordings = np.concatenate(recordings, axis=0)

    #save the recorded audio
    write("recording.wav", frequency, full_recordings)
    print("✅ Audio saved as 'recording.wav'")

    # Exit the program after saving
    sys.exit("🎤 Program exited after saving the recording.")

while True:
    try:
        if keyboard.is_pressed('r'):  # if key 'enter' is pressed
            start_recording()
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit()
    except Exception as e:
        print(f"Error: {e}")
        break

