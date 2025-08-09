import os
from bark import generate_audio, preload_models
import scipy.io.wavfile

def generate_narration(scenes, output_path="outputs/audio/narration.wav"):
    preload_models()
    combined_text = " ".join(scenes)
    audio_array = generate_audio(combined_text)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    scipy.io.wavfile.write(output_path, rate=22050, data=audio_array)
    return output_path
